from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import Activity, Patient
from ..forms import PatientForm

# this route to show patient by his id
@login_required(login_url='login')
def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient':patient}
    return render(request, 'base/patient.html', context)

# this route to create patient 
@login_required(login_url='login')
def createPatient(request, fk):
    form = PatientForm()
    activity = Activity.objects.get(id=fk)

    if request.user != activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            activity.num_of_patients += 1
            patient.Activity = activity
            activity.save()
            patient.save()
            messages.success(request, 'patient created successfully')
            return redirect('activity', pk=patient.Activity.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)

    if request.user != patient.Activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'patient updated successfully')
            return redirect('patient', pk=patient.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)

    if request.user != patient.Activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')
    
    if request.method == 'POST':
        try:
            patient.delete()
            messages.success(request, 'patient deleted successfully')
            return redirect('activity', pk=patient.Activity.id)
        except:
            messages.error(request, 'somthing went wrong!')
            return redirect('activity', pk=patient.Activity.id)
        
    context = {'obj': patient}
    return render(request, 'base/delete.html', context)
