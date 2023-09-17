from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Mobileclinic(models.Model):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    num_of_staff = models.IntegerField()
    Clinic_Services = (
        ("Health", "Health"),
        ("Education", "Education"),
    )
    clinic_services = models.CharField(max_length=10, choices=Clinic_Services)
    clinic_capacity = models.IntegerField()
    total_annual_budget = models.IntegerField()
    pharmaceutical_expenditure = models.IntegerField()
    pharmaceutical_waste = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Resources(models.Model):
    mobile_clinic = models.ForeignKey(Mobileclinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Type = (
        ("Health", "Health"),
        ("Education", "Education"),
        ("Finance", "Finance"),
    )
    type = models.CharField(max_length=10, choices=Type) 
    expiration_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class Activity(models.Model):
    mobile_clinic = models.ForeignKey(Mobileclinic, on_delete=models.SET_NULL, null=True) 
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    population_density = models.IntegerField()
    Crisis_Type = (
        ("Earthquake", "Earthquake"),
        ("Floods", "Floods"),
        ("Tornado", "Tornado"),
    )
    crisis_type = models.CharField(max_length=10, choices=Crisis_Type)
    status = models.CharField(max_length=20)
    num_of_patients = models.IntegerField()
    Weather_Status = (
        ("Cloudy", "Cloudy"),
        ("Sunny", "Sunny"),
        ("Rainy", "Rainy"),
    )
    weather_status = models.CharField(max_length=10, choices=Weather_Status)

    def location (self):
        loc = self.latitude +',' + self.longitude
        return loc
    
    def __str__(self):
        return str(self.date)
    
class Patient(models.Model):
    Activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    diagnosis = models.TextField()
    medication_date = models.DateField()

    def __str__(self):
        return self.diagnosis[0:50]

