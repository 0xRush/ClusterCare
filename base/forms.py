from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Mobileclinic, Activity, Resources, Patient
import datetime

class MobileclinicForm(ModelForm):
    class Meta:
        model = Mobileclinic
        fields = ['name', 'num_of_staff', 'clinic_services', 'clinic_capacity',
                  'total_annual_budget', 'pharmaceutical_expenditure', 'pharmaceutical_waste']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'latitude', 'longitude', 'population_density', 'crisis_type', 
                  'num_of_patients', 'weather_status']
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")

        if date > datetime.date.today():
            raise ValidationError("The Activity date can not be in the future")

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['name', 'type', 'expiration_date', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        expiration_date = cleaned_data.get("expiration_date")

        if expiration_date <= datetime.date.today():
            raise ValidationError("The expiration date can not be in the past")

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'gender', 'diagnosis', 'medication_date']

    def clean(self):
        cleaned_data = super().clean()
        medication_date = cleaned_data.get("medication_date")

        if medication_date > datetime.date.today():
            raise ValidationError("The medication date can not be in the future")
