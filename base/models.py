from django.db import models
from mongodb_connection import db
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    Role = (
        ("Manager", "Manager"),
        ("None", "None"),
    )
    role = models.CharField(max_length=20, choices=Role, null=True)

    REQUIRED_FIELDS = []


class Mobileclinic(models.Model):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=50)
    num_of_staff = models.PositiveIntegerField()
    Clinic_Services = (
        ("Emergency Medical Care", "Emergency Medical Care"),
        ("Wound Care", "Wound Care"),
        ("Infectious Disease Control", "Infectious Disease Control"),
        ("Mental Health Support", "Mental Health Support"),
        ("Rescue and Evacuation Support", "Rescue and Evacuation Support"),
        ("Health Education", "Health Education"),
    )
    clinic_services = models.CharField(max_length=100, choices=Clinic_Services)
    clinic_capacity = models.PositiveIntegerField()
    total_annual_budget = models.FloatField(validators=[MinValueValidator(0.0)])
    pharmaceutical_expenditure = models.FloatField(validators=[MinValueValidator(0.0)])
    pharmaceutical_waste = models.FloatField(validators=[MinValueValidator(0.0)])
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
        ("Medical Equipment", "Medical Equipment"),
        ("Medical Supplies", "Medical Supplies"),
        ("Vaccines and Immunization", "Vaccines and Immunization"),
        ("Diagnostic and Laboratory Equipment", "Diagnostic and Laboratory Equipment"),
        ("Pharmaceutical Supplies", "Pharmaceutical Supplies"),
        ("Emergency Response and Rescue Equipment", "Emergency Response and Rescue Equipment"),
    )
    type = models.CharField(max_length=100, choices=Type)
    expiration_date = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Activity(models.Model):
    mobile_clinic = models.ForeignKey(Mobileclinic, on_delete=models.CASCADE) 
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    population_density = models.PositiveIntegerField()
    Crisis_Type = (
        ("Earthquakes", "Earthquakes"),
        ("Tornadoes", "Tornadoes"),
        ("Floods", "Floods"),
        ("Wildfires", "Wildfires"),
        ("Droughts", "Droughts"),
        ("Tsunamis", "Tsunamis"),
        ("Volcanic Eruptions", "Volcanic Eruptions"),
        ("Pandemics", "Pandemics"),
        ("Food and Water Contamination", "Food and Water Contamination"),
        ("Financial Crises", "Financial Crises"),
        ("Refugee and Displacement Crises", "Refugee and Displacement Crises"),
        ("Food and Water Scarcity", "Food and Water Scarcity"),
        ("Healthcare Crises", "Healthcare Crises"),
    )
    crisis_type = models.CharField(max_length=100, choices=Crisis_Type)
    Status = (
        ("Active", "Active"),
        ("inActive", "inActive"),
    )
    status = models.CharField(max_length=20, choices=Status)
    num_of_patients = models.PositiveIntegerField()
    Weather_Status = (
        ("Clear Sky", "Clear Sky"),
        ("Cloudy", "Cloudy"),
        ("Partly Cloudy", "Partly Cloudy"),
        ("Fog", "Fog"),
        ("Rain", "Rain"),
        ("Snow", "Snow"),
        ("Sleet", "Sleet"),
        ("Thunderstorm", "Thunderstorm"),
        ("Tornado", "Tornado"),
        ("Blizzard", "Blizzard"),
        ("Heatwave", "Heatwave"),
        ("Dust Storm", "Dust Storm"),
    )
    weather_status = models.CharField(max_length=100, choices=Weather_Status)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def location (self):
        loc = self.latitude +',' + self.longitude
        return loc
    
    def __str__(self):
        return str(self.date)
    
class Patient(models.Model):
    Activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    age = models.PositiveIntegerField()
    Gender = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    gender = models.CharField(max_length=20, choices=Gender)
    Diagnosis = [
        ('E11', 'Type 2 Diabetes Mellitus'),
        ('I10', 'Hypertension'),
        ('F32', 'Major Depressive Disorder'),
        ('J20', 'Acute Bronchitis'),
        ('I10', 'Essential Hypertension'),
        ('M17', 'Osteoarthritis of Knee'),
        ('I21', 'Acute Myocardial Infarction'),
        ('J45', 'Asthma'),
        ('N39.0', 'Urinary Tract Infection'),
        ('M47.812', 'Cervical Spondylosis'),
    ]
    diagnosis = models.CharField(max_length=20, choices=Diagnosis)
    medication_date = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_icd_10_code(self):
        # Retrieve the ICD-10 code for the selected diagnosis type
        return dict(self.Diagnosis).get(self.diagnosis, '')
    
    def __str__(self):
        return self.diagnosis[0:50]

HistoricalActivity = db['Historical_activity']

PredictionActivity = db['Predition_Activity']