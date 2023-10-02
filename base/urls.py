from django.urls import path
from .views import views, clinicViews, activityViews, resourceViews, patientViews



urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),

    path('tips/', clinicViews.tips, name='tips'),
    path('dashboard/', clinicViews.dashboard, name='dashboard'),
    path('mobileclinic/<str:pk>', clinicViews.mobileclinic, name='mobileclinic'),
    path('create-mobileclinic/', clinicViews.createMobileClinic, name='create-mobileclinic'),
    path('update-mobileclinic/<str:pk>', clinicViews.updateMobileClinic, name='update-mobileclinic'),
    path('delete-mobileclinic/<str:pk>', clinicViews.deleteMobileClinic, name='delete-mobileclinic'),

    path('activity/<str:pk>', activityViews.activity, name='activity'),
    path('mobileclinic/<str:fk>/create-activity/', activityViews.createActivity, name='create-activity'),
    path('update-activity/<str:pk>', activityViews.updateActivity, name='update-activity'),
    path('delete-activity/<str:pk>', activityViews.deleteActivity, name='delete-activity'),

    path('resource/<str:pk>', resourceViews.resource, name='resource'),
    path('mobileclinic/<str:fk>/create-resource/', resourceViews.createResource, name='create-resource'),
    path('update-resource/<str:pk>', resourceViews.updateResource, name='update-resource'),
    path('delete-resource/<str:pk>', resourceViews.deleteResource, name='delete-resource'),

    path('patient/<str:pk>', patientViews.patient, name='patient'),
    path('activity/<str:fk>/create-patient/', patientViews.createPatient, name='create-patient'),
    path('update-patient/<str:pk>', patientViews.updatePatient, name='update-patient'),
    path('delete-patient/<str:pk>', patientViews.deletePatient, name='delete-patient'),
]