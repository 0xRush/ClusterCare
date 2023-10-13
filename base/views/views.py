from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from ..models import Mobileclinic, Activity, User
from ..forms import MyUserCreationForm
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
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
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
    activities = Activity.objects.all()

    Map = folium.Map(location=[23.8859, 45.0792], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(Map)
    
    for activity in activities:
        if activity.status == 'Active':
            folium.Marker(
                location=[activity.latitude, activity.longitude],
                popup=f"""<h5><a href=mobileclinic/{activity.mobile_clinic.id} target=_top>{activity.mobile_clinic.name}</a></h5>
                          <p>manager: {activity.mobile_clinic.manager}<p>
                          <p>clinic_services: {activity.mobile_clinic.clinic_services}</p>
                          <p>clinic_capacity: {activity.mobile_clinic.clinic_capacity}</p>
                          <p>num_of_patients: {activity.num_of_patients}</p>
                          <p>date: {activity.date}</p>""",
                icon=folium.Icon(color="green", icon="ok-sign"),
            ).add_to(marker_cluster)

    context = {'map': Map._repr_html_()}
    return render(request, 'base/home.html', context)

