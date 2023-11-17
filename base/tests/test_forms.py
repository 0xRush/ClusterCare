from ..forms import MyUserCreationForm, MobileclinicForm, ActivityForm, ResourceForm, PatientForm
from django.test import TestCase
from datetime import datetime


class TestForms(TestCase):

    def test_UserCreation_form_valid_data(self):
        form = MyUserCreationForm(data={ 
            'name': 'testo',
            'username': 'testoo',
            'email': 'test0@gmail.com',
            'password1': 't12345678',
            'password2': 't12345678'
            })
        
        self.assertTrue(form.is_valid())

    def test_UserCreation_form_no_data(self):
        form = MyUserCreationForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_mobileclinic_form_valid_data(self):
        form = MobileclinicForm(data={
            'manager': 1,
            'name':'test Mobile Clinic form',
            'num_of_staff':5,
            'clinic_services':'Emergency Medical Care',
            'clinic_capacity':50,
            'total_annual_budget':10000,
            'pharmaceutical_expenditure':2000,
            'pharmaceutical_waste':100
            })
        
        self.assertTrue(form.is_valid())
        
    def test_mobileclinic_form_no_data(self):
        form = MobileclinicForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_resource_form_valid_data(self):
        form = ResourceForm(data={
            'mobile_clinic': 1,
            'name': 'test Resource',
            'type': 'Medical Equipment',
            'expiration_date': datetime.strptime('2024-02-01', "%Y-%m-%d").date(),
            'quantity': 10
        })
        
        self.assertTrue(form.is_valid())

    def test_resource_form_no_data(self):
        form = ResourceForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_activity_form_valid_data(self):
        form = ActivityForm(data={
            'mobile_clinic': 1,
            'date': datetime.strptime('2023-02-01', "%Y-%m-%d").date(),
            'latitude': 123.456,
            'longitude': 789.012,
            'population_density': 100,
            'crisis_type': 'Earthquakes',
            'status': 'Active',
            'num_of_patients': 50,
            'weather_status': 'Clear Sky'
        })
        
        self.assertTrue(form.is_valid())
    
    def test_activity_form_no_data(self):
        form = ActivityForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_patient_form_valid_data(self):
        form = PatientForm(data={
            'Activity': 1,
            'age': 25,
            'gender': 'Male',
            'diagnosis': 'Test Diagnosis',
            'medication_date': datetime.strptime('2023-02-01', "%Y-%m-%d").date()
        })
        
        self.assertTrue(form.is_valid())
    
    def test_patient_form_no_data(self):
        form = PatientForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)