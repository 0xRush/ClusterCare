from django.forms import ModelForm
from .models import Mobileclinic, Activity, Resources, Patient

class MobileclinicForm(ModelForm):
    class Meta:
        model = Mobileclinic
        fields = ['name', 'num_of_staff', 'clinic_services', 'clinic_capacity',
                  'total_annual_budget', 'pharmaceutical_expenditure', 'pharmaceutical_waste']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'latitude', 'longitude', 'population_density', 'crisis_type', 
                  'status', 'num_of_patients', 'weather_status']

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['name', 'type', 'expiration_date', 'quantity']

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'gender', 'diagnosis', 'medication_date']
