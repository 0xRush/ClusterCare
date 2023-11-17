from django.test import TestCase, Client
from django.urls import reverse
from ..models import User, Mobileclinic, Resources, Activity, Patient
from datetime import datetime

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')
        self.tips_url = reverse('tips')
        self.dashboard_url = reverse('dashboard')
        self.mobileclinic_url = reverse('mobileclinic', args=[1])
        self.create_mobileclinic_url = reverse('create-mobileclinic')
        self.update_mobileclinic_url = reverse('update-mobileclinic', args=[1])
        self.delete_mobileclinic_url = reverse('delete-mobileclinic', args=[1])
        self.activity_url = reverse('activity', args=[1])
        self.create_activity_url = reverse('create-activity', args=[1])
        self.update_activity_url = reverse('update-activity', args=[1])
        self.delete_activity_url = reverse('delete-activity', args=[1])
        self.resource_url = reverse('resource', args=[1])
        self.create_resource_url = reverse('create-resource', args=[1])
        self.update_resource_url = reverse('update-resource', args=[1])
        self.delete_resource_url = reverse('delete-resource', args=[1])
        self.patient_url = reverse('patient', args=[1])
        self.create_patient_url = reverse('create-patient', args=[1])
        self.update_patient_url = reverse('update-patient', args=[1])
        self.delete_patient_url = reverse('delete-patient', args=[1])

        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword', role='Manager')
        self.client.login(username='testuser', password='testpassword')

        self.mobileclinic = Mobileclinic.objects.create(
            manager=self.user,
            name='Test Mobile Clinic',
            num_of_staff=5,
            clinic_services='Emergency Medical Care',
            clinic_capacity=50,
            total_annual_budget=100000,
            pharmaceutical_expenditure=20000,
            pharmaceutical_waste=1000
        )

        self.resource = Resources.objects.create(
            mobile_clinic=self.mobileclinic,
            name='Test Resource',
            type='Medical Equipment',
            expiration_date='2024-01-01',
            quantity=10
        )

        self.activity = Activity.objects.create(
            mobile_clinic=self.mobileclinic,
            date='2023-01-01',
            latitude=123.456,
            longitude=789.012,
            population_density=100,
            crisis_type='Earthquakes',
            status='Active',
            num_of_patients=50,
            weather_status='Clear Sky'
        )

        self.patient = Patient.objects.create(
            Activity=self.activity,
            age=25,
            gender='Male',
            diagnosis='Test Diagnosis',
            medication_date='2023-01-01'
        )

    # ===========================================================================================
   
    def test_logout(self):
        self.client.logout()
        
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, 302)

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 302)

    def test_login_POST(self):
        user = { 'username': 'testuser', 'password': 'testpassword'}

        response = self.client.post(self.login_url, user)
        
        self.assertEqual(response.status_code, 302)

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login_register.html')

    def test_register_POST(self):
        user = { 'name': 'test', 'username': 'testt', 'email': 'test@gmail.com', 'password1': 't123456789', 'password2': 't123456789'}
        response = self.client.post(self.register_url, user)
        
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_dashboard(self):
        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/dashboard.html')

    def test_tips(self):
        response = self.client.get(self.tips_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/tips.html')
    
    # ===========================================================================================

    def test_mobileclinic(self):
        response = self.client.get(self.mobileclinic_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic.html')

    def test_create_mobileclinic_GET(self):
        response = self.client.get(self.create_mobileclinic_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')

    def test_create_mobileclinic_POST(self):
        mobileclinic = {
            'manager':self.user,
            'name':'test Mobile Clinic',
            'num_of_staff':5,
            'clinic_services':'Emergency Medical Care',
            'clinic_capacity':50,
            'total_annual_budget':100000,
            'pharmaceutical_expenditure':20000,
            'pharmaceutical_waste':1000}
        
        response = self.client.post(self.create_mobileclinic_url, mobileclinic)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(mobileclinic['name'], 'test Mobile Clinic')

    def test_update_mobileclinic_GET(self):
        response = self.client.get(self.update_mobileclinic_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')
    
    def test_update_mobileclinic_POST(self):
        mobileclinic = {
            'manager':self.user,
            'name':'test Mobile Clinic',
            'num_of_staff':5,
            'clinic_services':'Emergency Medical Care',
            'clinic_capacity':50,
            'total_annual_budget':100000,
            'pharmaceutical_expenditure':20000,
            'pharmaceutical_waste':1000}
        
        response = self.client.post(self.update_mobileclinic_url, mobileclinic)

        self.assertEqual(response.status_code, 302)
        
    def test_delete_mobileclinic_GET(self):
        response = self.client.get(self.delete_mobileclinic_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/delete.html')

    def test_delete_mobileclinic_POST(self):
        response = self.client.post(self.delete_mobileclinic_url)

        self.assertEqual(response.status_code, 302)

    # ===========================================================================================

    def test_resource(self):
        response = self.client.get(self.resource_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/resource.html')

    def test_create_resource_GET(self):
        response = self.client.get(self.create_resource_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')

    def test_create_resource_POST(self):
        resource = {
            'mobile_clinic': self.mobileclinic,
            'name': 'test Resource',
            'type': 'Medical Equipment',
            'expiration_date': '2024-01-01',
            'quantity': 10
        }

        response = self.client.post(self.create_resource_url, resource)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(resource['name'], 'test Resource')

    def test_update_resource_GET(self):
        response = self.client.get(self.update_resource_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')
    
    def test_update_resource_POST(self):
        resource = {
            'mobile_clinic': self.mobileclinic,
            'name': 'test Resource',
            'type': 'Medical Equipment',
            'expiration_date': '2024-01-01',
            'quantity': 10
        }

        response = self.client.post(self.update_resource_url, resource)

        self.assertEqual(response.status_code, 302)
        
    def test_delete_resource_GET(self):
        response = self.client.get(self.delete_resource_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/delete.html')

    def test_delete_resource_POST(self):
        response = self.client.post(self.delete_resource_url)

        self.assertEqual(response.status_code, 302)

    # ===========================================================================================   

    def test_activity(self):
        response = self.client.get(self.activity_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/activity.html')

    def test_create_activity_GET(self):
        response = self.client.get(self.create_activity_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')

    def test_create_activity_POST(self):
        activity = {
            'mobile_clinic': self.mobileclinic,
            'date': '2023-01-01',
            'latitude': 123.456,
            'longitude': 789.012,
            'population_density': 100,
            'crisis_type': 'Earthquakes',
            'status': 'Active',
            'num_of_patients': 50,
            'weather_status': 'Clear Sky'
        }
            
        response = self.client.post(self.create_activity_url, activity)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(activity['status'], 'Active')

    def test_update_activity_GET(self):
        response = self.client.get(self.update_activity_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')
    
    def test_update_activity_POST(self):
        activity = {
            'mobile_clinic': self.mobileclinic,
            'date': '2023-01-01',
            'latitude': 123.456,
            'longitude': 789.012,
            'population_density': 100,
            'crisis_type': 'Earthquakes',
            'status': 'Active',
            'num_of_patients': 50,
            'weather_status': 'Clear Sky'
        }
        
        response = self.client.post(self.update_activity_url, activity)

        self.assertEqual(response.status_code, 302)
        
    def test_delete_activity_GET(self):
        response = self.client.get(self.delete_activity_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/delete.html')

    def test_delete_activity_POST(self):
        response = self.client.post(self.delete_activity_url)

        self.assertEqual(response.status_code, 302)

    # ===========================================================================================   
    
    def test_patient(self):
        response = self.client.get(self.patient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/patient.html')

    def test_create_patient_GET(self):
        response = self.client.get(self.create_patient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')

    def test_create_patient_POST(self):
        patient = {
            'Activity': self.activity,
            'age': 25,
            'gender': 'Male',
            'diagnosis': 'Test Diagnosis',
            'medication_date': '2023-01-01'
        }
            
        response = self.client.post(self.create_patient_url, patient)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(patient['age'], 25)

    def test_update_patient_GET(self):
        response = self.client.get(self.update_patient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/mobileclinic_form.html')
    
    def test_update_patient_POST(self):
        patient = {
            'Activity': self.activity,
            'age': 25,
            'gender': 'Male',
            'diagnosis': 'Test Diagnosis',
            'medication_date': '2023-01-01'
        }

        response = self.client.post(self.update_patient_url, patient)

        self.assertEqual(response.status_code, 302)
        
    def test_delete_patient_GET(self):
        response = self.client.get(self.delete_patient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/delete.html')

    def test_delete_patient_POST(self):
        response = self.client.post(self.delete_patient_url)

        self.assertEqual(response.status_code, 302)