from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from ..models import Mobileclinic, Activity, Resources
from ..forms import MobileclinicForm

# this route to show statistics for mobile clinic
@login_required(login_url='login')
def tips(request):
    return render(request, 'base/tips.html')

# this route to all mobile clinics
@login_required(login_url='login')
def dashboard(request):
    mobileclinics = Mobileclinic.objects.all()
    context = {'mobileclinics': mobileclinics}
    return render(request, 'base/dashboard.html', context)

# this route to show a single mobile clinc by it's id
@login_required(login_url='login')
def mobileclinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    activities = Activity.objects.filter(mobile_clinic=mobileclinic)
    resources = Resources.objects.filter(mobile_clinic=mobileclinic)
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
            mobileclinic.save()
            return redirect('dashboard')

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
            form.save()
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
        mobileclinic.delete()
        return redirect('dashboard')
    
    context = {'obj': mobileclinic }
    return render(request, 'base/delete.html', context)