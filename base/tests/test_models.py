from django.test import TestCase
from ..models import User, Mobileclinic, Resources, Activity, Patient

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword', role='Manager')

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

    def test_mobileClinic_model_is_working(self):
        mobileclinic2 = Mobileclinic.objects.create(
        manager=self.user,
        name='test Mobile Clinic',
        num_of_staff=5,
        clinic_services='Emergency Medical Care',
        clinic_capacity=50,
        total_annual_budget=100000,
        pharmaceutical_expenditure=20000,
        pharmaceutical_waste=1000
    )
        
        self.assertEquals(mobileclinic2.name, 'test Mobile Clinic')

    def test_resource_model_is_working(self):
        resource = Resources.objects.create(
            mobile_clinic=self.mobileclinic,
            name='Test Resource',
            type='Medical Equipment',
            expiration_date='2024-01-01',
            quantity=10
        )
        
        self.assertEquals(resource.name, 'Test Resource')

    def test_activity_model_is_working(self):
        activity = Activity.objects.create(
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
        
        self.assertEquals(activity.status, 'Active')

    def test_patient_model_is_working(self):
        activity = self.test_activity_model_is_working()

        patient = Patient.objects.create(
            Activity= activity,
            age=25,
            gender='Male',
            diagnosis='Test Diagnosis',
            medication_date='2023-01-01'
        )

        self.assertEquals(patient.diagnosis, 'Test Diagnosis')