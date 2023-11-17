from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views.clinicViews import tips, dashboard, mobileclinic, createMobileClinic, updateMobileClinic, deleteMobileClinic
from ..views.activityViews import activity, createActivity, updateActivity, deleteActivity
from ..views.resourceViews import resource, createResource, updateResource, deleteResource
from ..views.patientViews import patient, createPatient, updatePatient, deletePatient
from ..views.views import home, loginPage, logoutUser, registerPage

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginPage)

    def test_register_url_is_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registerPage)

    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutUser)

    def test_tips_url_is_resolves(self):
        url = reverse('tips')
        self.assertEqual(resolve(url).func, tips)

    def test_dashboard_url_is_resolves(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_mobileclinic_url_is_resolves(self):
        url = reverse('mobileclinic', args=[1])
        self.assertEqual(resolve(url).func, mobileclinic)
    
    def test_createmobileclinic_url_is_resolves(self):
        url = reverse('create-mobileclinic')
        self.assertEqual(resolve(url).func, createMobileClinic)
    
    def test_updatemobileclinic_url_is_resolves(self):
        url = reverse('update-mobileclinic', args=[1])
        self.assertEqual(resolve(url).func, updateMobileClinic)

    def test_deletemobileclinic_url_is_resolves(self):
        url = reverse('delete-mobileclinic', args=[1])
        self.assertEqual(resolve(url).func, deleteMobileClinic)

    def test_activity_url_is_resolves(self):
        url = reverse('activity', args=[1])
        self.assertEqual(resolve(url).func, activity)
    
    def test_createactivity_url_is_resolves(self):
        url = reverse('create-activity', args=[1])
        self.assertEqual(resolve(url).func, createActivity)
    
    def test_updateactivity_url_is_resolves(self):
        url = reverse('update-activity', args=[1])
        self.assertEqual(resolve(url).func, updateActivity)

    def test_deleteactivity_url_is_resolves(self):
        url = reverse('delete-activity', args=[1])
        self.assertEqual(resolve(url).func, deleteActivity)

    def test_resource_url_is_resolves(self):
        url = reverse('resource', args=[1])
        self.assertEqual(resolve(url).func, resource)
    
    def test_createresource_url_is_resolves(self):
        url = reverse('create-resource', args=[1])
        self.assertEqual(resolve(url).func, createResource)
    
    def test_updateresource_url_is_resolves(self):
        url = reverse('update-resource', args=[1])
        self.assertEqual(resolve(url).func, updateResource)

    def test_deleteresource_url_is_resolves(self):
        url = reverse('delete-resource', args=[1])
        self.assertEqual(resolve(url).func, deleteResource)

    def test_patient_url_is_resolves(self):
        url = reverse('patient', args=[1])
        self.assertEqual(resolve(url).func, patient)
    
    def test_createpatient_url_is_resolves(self):
        url = reverse('create-patient', args=[1])
        self.assertEqual(resolve(url).func, createPatient)
    
    def test_updatepatient_url_is_resolves(self):
        url = reverse('update-patient', args=[1])
        self.assertEqual(resolve(url).func, updatePatient)

    def test_deletepatient_url_is_resolves(self):
        url = reverse('delete-patient', args=[1])
        self.assertEqual(resolve(url).func, deletePatient)