from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import Mobileclinic, Activity, Patient
from ..forms import ActivityForm
import streamlit as st
from streamlit_folium import folium_static
import folium

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

    page = 'createActivity'

    map = folium.Map(location=[23.8859, 45.0792], zoom_start=5, width=500, height=500)
    map.add_child(folium.LatLngPopup())
    folium_static(map)

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        
        if form.is_valid():
            mobileclinic = Mobileclinic.objects.get(id=fk)
            try:
                oldActivity = Activity.objects.get(mobile_clinic=mobileclinic, status='Active')
                oldActivity.status = 'inActive'
                oldActivity.save()
            except:
                print('no activity found')
                
            activity = form.save(commit=False)
            activity.status = 'Active'
            activity.mobile_clinic = mobileclinic
            if request.user != activity.mobile_clinic.manager:
                messages.error(request, 'you are not allowed here')
                return redirect('home')
            else:
                activity.save()
                return redirect('mobileclinic', pk=activity.mobile_clinic.id)
    
    context = {'form': form, 'map':map._repr_html_(), 'page': page}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def updateActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    form = ActivityForm(instance=activity)

    if request.user != activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity', pk=activity.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)

    if request.user != activity.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        activity.delete()
        return redirect('mobileclinic', pk=activity.mobile_clinic.id)
    
    context = {'obj': activity}
    return render(request, 'base/delete.html', context)