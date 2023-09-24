from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Mobileclinic, Activity, Resources, Patient
from .forms import MobileclinicForm, ActivityForm, ResourceForm, PatientForm
import folium
from folium.plugins import MarkerCluster


# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usernme OR Password does not exist")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registeration')

    context = {'form':form}
    return render(request, 'base/login_register.html', context)


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
            form.save()
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

# this route to show an activity by it's id
@login_required(login_url='login')
def activity(request, pk):
    activity = Activity.objects.get(id=pk)
    patients = Patient.objects.filter(Activity=activity)
    context = {'activity': activity, 'patients': patients}
    return render(request, 'base/activity.html', context)

# this route to create activity
@login_required(login_url='login')
def createActivity(request):
    form = ActivityForm()

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            if request.user != activity.mobile_clinic.manager:
                messages.error(request, 'you are not allowed here')
                return redirect('home')
            else:
                activity.save()
                return redirect('mobileclinic', pk=activity.mobile_clinic.id)

    context = {'form': form}
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

# this route to show resource by it's id
@login_required(login_url='login')
def resource(request, pk):
    resource = Resources.objects.get(id=pk)
    context = {'resource': resource}
    return render(request, 'base/resource.html', context)

# this route to ceate resource
@login_required(login_url='login')
def createResource(request):
    form = ResourceForm()

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            if request.user != resource.mobile_clinic.manager:
                messages.error(request, 'you are not allowed here')
                return redirect('home')
            else:
                resource.save()
                return redirect('mobileclinic', pk=resource.mobile_clinic.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def updateResource(request, pk):
    resource = Resources.objects.get(id=pk)
    form = ResourceForm(instance=resource)

    if request.user != resource.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')
    
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource', pk=resource.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deleteResource(request, pk):
    resource = Resources.objects.get(id=pk)

    if request.user != resource.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        resource.delete()
        return redirect('mobileclinic', pk=resource.mobile_clinic.id)
    
    context = {'obj': resource}
    return render(request, 'base/delete.html', context)

# this route to show patient by his id
@login_required(login_url='login')
def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {'patient':patient}
    return render(request, 'base/patient.html', context)

# this route to create patient 
@login_required(login_url='login')
def createPatient(request):
    form = PatientForm()
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            if request.user != patient.Activity.mobile_clinic.manager:
                messages.error(request, 'you are not allowed here')
                return redirect('home')
            else:
                patient.save()
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
        patient.delete()
        return redirect('activity', pk=patient.Activity.id)
    
    context = {'obj': patient}
    return render(request, 'base/delete.html', context)


