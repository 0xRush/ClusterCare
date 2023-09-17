from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mobileclinic, Activity, Resources, Patient
from .forms import MobileclinicForm, ActivityForm, ResourceForm, PatientForm


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

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
            return redirect(f"/mobileclinic/{pk}")

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

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
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

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
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

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
            form.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)


