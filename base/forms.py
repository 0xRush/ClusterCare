from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Mobileclinic, Activity, Resources, Patient, User
import datetime
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.widgets.TextInput(attrs={"placeholder":"Enter your Name",
                  "class":"form-control"}),
            'username': forms.widgets.TextInput(attrs={"placeholder":"Enter your userName",
                  "class":"form-control"}),
            'email': forms.widgets.EmailInput(attrs={"placeholder":"Enter your Email",
                  "class":"form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder":"Enter your Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder":"Confirm your Password"})

class MobileclinicForm(ModelForm):
    class Meta:
        model = Mobileclinic
        fields = ['name', 'num_of_staff', 'clinic_services', 'clinic_capacity',
                  'total_annual_budget', 'pharmaceutical_expenditure']
        widgets = {
            'name': forms.widgets.TextInput(attrs={"placeholder":"Enter your Name",
                  "class": "form-control"}),
            'num_of_staff': forms.widgets.NumberInput(attrs={"class": "form-control"}),
            'clinic_services': forms.widgets.Select(attrs={"class": "form-control"}),
            'clinic_capacity': forms.widgets.NumberInput(attrs={"class": "form-control"}),
            'total_annual_budget': forms.widgets.NumberInput(attrs={"class": "form-control"}),
            'pharmaceutical_expenditure': forms.widgets.NumberInput(attrs={"class": "form-control"}),
        }

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'latitude', 'longitude', 'population_density', 'crisis_type', 
                  'weather_status']
        widgets = {
            'date': forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
            'latitude': forms.widgets.HiddenInput(attrs={"class": "form-control"}),
            'longitude': forms.widgets.HiddenInput(attrs={"class": "form-control"}),
            'population_density': forms.widgets.NumberInput(attrs={"class": "form-control"}),
            'crisis_type': forms.widgets.Select(attrs={"class": "form-control"}),
            'weather_status': forms.widgets.Select(attrs={"class": "form-control"}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")

        if date != None and date > datetime.date.today():
            raise ValidationError("The Activity date can not be in the future")

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['name', 'type', 'expiration_date', 'quantity']
        widgets = {
                'name': forms.widgets.TextInput(attrs={"class": "form-control"}),
                'type': forms.widgets.Select(attrs={"class": "form-control"}),
                'expiration_date': forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
                'quantity': forms.widgets.NumberInput(attrs={"class": "form-control"}),
            }

    def clean(self):
        cleaned_data = super().clean()
        expiration_date = cleaned_data.get("expiration_date")

        if expiration_date != None and expiration_date <= datetime.date.today():
            raise ValidationError("The expiration date can not be in the past")
            

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'gender', 'diagnosis', 'medication_date']
        widgets = {
                'age': forms.widgets.NumberInput(attrs={"class": "form-control"}),
                'gender': forms.widgets.Select(attrs={"class": "form-control"}),
                'diagnosis': forms.widgets.Select(attrs={"class": "form-control"}),
                'medication_date': forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
            }

    def clean(self):
        cleaned_data = super().clean()
        medication_date = cleaned_data.get("medication_date")

        if medication_date != None and medication_date > datetime.date.today():
            raise ValidationError("The medication date can not be in the future")
