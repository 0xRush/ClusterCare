from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from ..models import Mobileclinic, Activity
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
    mobileclinics = Mobileclinic.objects.all()
    
    Map = folium.Map(location=[23.8859, 45.0792], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(Map)

    for activity in activities:
        if activity.status == 'Active':
            folium.Marker(
                location=[activity.latitude, activity.longitude],
                popup=f"<a href=mobileclinic/{activity.mobile_clinic.id} target=_top>{activity.mobile_clinic.name}</a>",
                icon=folium.Icon(color="green", icon="ok-sign"),
            ).add_to(marker_cluster)

    context = {'mobileclinics': mobileclinics, 'activities': activities, 'map': Map._repr_html_()}
    return render(request, 'base/home.html', context)

