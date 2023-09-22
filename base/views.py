from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mobileclinic, Activity, Resources, Patient
from .forms import MobileclinicForm, ActivityForm, ResourceForm, PatientForm
import folium
from folium.plugins import MarkerCluster


# Create your views here.
def home(request):
    activities = Activity.objects.select_related('mobile_clinic').all()
    
    Map = folium.Map(location=[23.8859, 45.0792], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(Map)

    for activity in activities:
        folium.Marker(
            location=[activity.latitude, activity.longitude],
            popup=f"<a href=mobileclinic/{activity.mobile_clinic.id} target=_top>{activity.mobile_clinic.name}</a>",
            icon=folium.Icon(color="green", icon="ok-sign"),
        ).add_to(marker_cluster)

    context = {'activities': activities, 'map': Map._repr_html_()}
    return render(request, 'base/home.html', context)

# this route to show statistics for mobile clinic
def tips(request):
    return render(request, 'base/tips.html')

# this route to all mobile clinics
def dashboard(request):
    mobileclinics = Mobileclinic.objects.all()
    context = {'mobileclinics': mobileclinics}
    return render(request, 'base/dashboard.html', context)

# this route to show a single mobile clinc by it's id
def mobileclinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    activities = Activity.objects.filter(mobile_clinic=mobileclinic)
    resources = Resources.objects.filter(mobile_clinic=mobileclinic)
    context = {'mobileclinic': mobileclinic, 'activities': activities, 'resources': resources}
    return render(request, 'base/mobileclinic.html', context)

# this route create mobile clinic
def createMobileClinic(request):
    form = MobileclinicForm()

    if request.method == 'POST':
        form = MobileclinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

# this route to update mobile clinic by it's id
def updateMobileClinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)
    form = MobileclinicForm(instance=mobileclinic)

    if request.method == 'POST':
        form = MobileclinicForm(request.POST, instance=mobileclinic)
        if form.is_valid():
            form.save()
            return redirect('mobileclinic', pk=mobileclinic.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)


def deleteMobileClinic(request, pk):
    mobileclinic = Mobileclinic.objects.get(id=pk)

    if request.method == 'POST':
        mobileclinic.delete()
        return redirect('dashboard')
    
    context = {'obj': mobileclinic }
    return render(request, 'base/delete.html', context)

# this route to show an activity by it's id
def activity(request, pk):
    activity = Activity.objects.get(id=pk)
    patients = Patient.objects.filter(Activity=activity)
    context = {'activity': activity, 'patients': patients}
    return render(request, 'base/activity.html', context)

# this route to create activity
def createActivity(request):
    form = ActivityForm()

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('mobileclinic', pk=activity.mobile_clinic.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def updateActivity(request, pk):
    activity = Activity.objects.get(id=pk)
    form = ActivityForm(instance=activity)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity', pk=activity.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def deleteActivity(request, pk):
    activity = Activity.objects.get(id=pk)

    if request.method == 'POST':
        activity.delete()
        return redirect('mobileclinic', pk=activity.mobile_clinic.id)
    
    context = {'obj': activity}
    return render(request, 'base/delete.html', context)

# this route to show resource by it's id
def resource(request, pk):
    resource = Resources.objects.get(id=pk)
    context = {'resource': resource}
    return render(request, 'base/resource.html', context)

# this route to ceate resource
def createResource(request):
    form = ResourceForm()

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save()
            return redirect('mobileclinic', pk=resource.mobile_clinic.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def updateResource(request, pk):
    resource = Resources.objects.get(id=pk)
    form = ResourceForm(instance=resource)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource', pk=resource.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def deleteResource(request, pk):
    resource = Resources.objects.get(id=pk)

    if request.method == 'POST':
        resource.delete()
        return redirect('mobileclinic', pk=resource.mobile_clinic.id)
    
    context = {'obj': resource}
    return render(request, 'base/delete.html', context)

# this route to show patient by his id
def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient':patient}
    return render(request, 'base/patient.html', context)

# this route to create patient 
def createPatient(request):
    form = PatientForm()
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('activity', pk=patient.Activity.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient', pk=patient.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)

    if request.method == 'POST':
        patient.delete()
        return redirect('activity', pk=patient.Activity.id)
    
    context = {'obj': patient}
    return render(request, 'base/delete.html', context)


