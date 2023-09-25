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
        fields = '__all__'

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = '__all__'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
