from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import Mobileclinic, Activity, Patient
from ..forms import ActivityForm


# this route to show an activity by it's id
@login_required(login_url='login')
def activity(request, pk):
    activity = Activity.objects.get(id=pk)
    patients = Patient.objects.filter(Activity=activity)
    context = {'activity': activity, 'patients': patients}
    return render(request, 'base/activity.html', context)

# this route to create activity
@login_required(login_url='login')
def createActivity(request, fk):
    form = ActivityForm()
    mobileclinic = Mobileclinic.objects.get(id=fk)
    page = 'createActivity'

    if request.user != mobileclinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        
        if form.is_valid():
            try:
                oldActivity = Activity.objects.get(mobile_clinic=mobileclinic, status='Active')
                oldActivity.status = 'inActive'
                oldActivity.save()
            except:
                print('no activity found')
                
            activity = form.save(commit=False)
            activity.status = 'Active'
            activity.num_of_patients = 0
            activity.mobile_clinic = mobileclinic
            activity.save()
            messages.success(request, 'activity created successfully')
            return redirect('mobileclinic', pk=activity.mobile_clinic.id)
        
    context = {'form': form, 'page': page}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def updateActivity(request, pk):
    page = 'updateActivity'
    activity = Activity.objects.get(id=pk)
    form = ActivityForm(instance=activity)

    if request.user != activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            try:
                oldActivity = Activity.objects.get(mobile_clinic=activity.mobile_clinic, status='Active')
                oldActivity.status = 'inActive'
                oldActivity.save()
            except:
                print('no activity found')

            activity = form.save(commit=False)
            activity.status = 'Active'
            activity.save()
            messages.success(request, 'activity updated successfully')
            return redirect('activity', pk=activity.id)
        
    context = {'form': form, 'page': page}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)

    if request.user != activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        try:
            activity.delete()
            messages.success(request, 'activity deleted successfully')
            return redirect('mobileclinic', pk=activity.mobile_clinic.id)
        except:
            messages.error(request, 'somthing went wrong!')
            return redirect('mobileclinic', pk=activity.mobile_clinic.id)
    
    context = {'obj': activity}
    return render(request, 'base/delete.html', context)