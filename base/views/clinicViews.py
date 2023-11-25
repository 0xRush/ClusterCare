from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import Mobileclinic, Activity, Resources
from ..forms import MobileclinicForm
from django.utils import timezone
from datetime import timedelta
from ..seeding.ML_tst import change_data, testML
from ..seeding.ML_predection import predection_data

# this route to show statistics for mobile clinic
@login_required(login_url='login')
def tips(request):
    mobileclinics = Mobileclinic.objects.filter(manager=request.user, pharmaceutical_waste__gt=0)
    two_months_ago = timezone.now() - timedelta(days=60)
    resources = Resources.objects.filter(mobile_clinic__in=mobileclinics, expiration_date__gte=two_months_ago)
    context = {'mobileclinics': mobileclinics, 'resources': resources}
    return render(request, 'base/tips.html', context)

# this route to all mobile clinics
@login_required(login_url='login')
def dashboard(request):
    mobileclinics = Mobileclinic.objects.filter(manager=request.user)
    context = {'mobileclinics': mobileclinics}
    return render(request, 'base/dashboard.html', context)

# this route to show a single mobile clinc by it's id
@login_required(login_url='login')
def mobileclinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    activities = Activity.objects.filter(mobile_clinic=mobileclinic)
    resources = Resources.objects.filter(mobile_clinic=mobileclinic)
    
    if request.method == 'POST':
        if request.user != mobileclinic.manager:
            try:
                clinic = Mobileclinic.objects.get(id=request.POST.get('selected_clinic'))
                if clinic.total_annual_budget >= mobileclinic.pharmaceutical_waste:
                    clinic.total_annual_budget = clinic.total_annual_budget - float(request.POST.get('donation'))
                    if clinic.pharmaceutical_expenditure > clinic.total_annual_budget:
                        clinic.pharmaceutical_waste = clinic.pharmaceutical_expenditure - clinic.total_annual_budget
                    mobileclinic.total_annual_budget += float(request.POST.get('donation'))
                    mobileclinic.pharmaceutical_waste -= float(request.POST.get('donation'))
                    mobileclinic.save()
                    clinic.save()
                    messages.success(request, 'Thank you')
                    return redirect('mobileclinic', pk=mobileclinic.id)
            except:
                messages.error(request, 'Somthing went wrong!')
                return redirect('mobileclinic', pk=mobileclinic.id)
        else:
            messages.error(request, 'Somthing went wrong!')
            return redirect('mobileclinic', pk=mobileclinic.id)

    context = {'mobileclinic': mobileclinic, 'activities': activities, 'resources': resources}
    return render(request, 'base/mobileclinic.html', context)

# this route create mobile clinic
@login_required(login_url='login')
def createMobileClinic(request):
    form = MobileclinicForm()

    if request.method == 'POST':
        form = MobileclinicForm(request.POST)
        if form.is_valid():
            mobileclinic = form.save(commit=False)
            mobileclinic.manager = request.user
            if mobileclinic.pharmaceutical_expenditure > mobileclinic.total_annual_budget:
                mobileclinic.pharmaceutical_waste = mobileclinic.pharmaceutical_expenditure - mobileclinic.total_annual_budget
            else:
                mobileclinic.pharmaceutical_waste = 0
            mobileclinic.save()
            messages.success(request, 'mobile clinic created successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Somthing went wrong!')
            return redirect('create-mobileclinic')
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

# this route to update mobile clinic by it's id
@login_required(login_url='login')
def updateMobileClinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    form = MobileclinicForm(instance=mobileclinic)

    if request.user != mobileclinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = MobileclinicForm(request.POST, instance=mobileclinic)
        if form.is_valid():
            clinic = form.save(commit=False)
            if clinic.pharmaceutical_expenditure > clinic.total_annual_budget:
                clinic.pharmaceutical_waste = clinic.pharmaceutical_expenditure - clinic.total_annual_budget
            else:
                clinic.pharmaceutical_waste = 0
            clinic.save()
            messages.success(request, 'mobile clinic updated successfully')
            return redirect('mobileclinic', pk=mobileclinic.id)
        else:
            messages.error(request, 'Somthing went wrong!')
            return redirect('mobileclinic', pk=mobileclinic.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deleteMobileClinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)

    if request.user != mobileclinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')
    
    if request.method == 'POST':
        try:
            mobileclinic.delete()
            messages.success(request, 'mobile clinic deleted successfully')
            return redirect('dashboard')
        except:
            messages.error(request, 'Somthing went wrong!')
            return redirect('dashboard')
    
    context = {'obj': mobileclinic }
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def test_clinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    data = change_data(mobileclinic)
    test = testML(data)
    predection = predection_data(test)

    return HttpResponse(predection)
    