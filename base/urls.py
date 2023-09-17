from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tips/', views.tips, name='tips'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('mobileclinic/<str:pk>', views.mobileclinic, name='mobileclinic'),
    path('create-mobileclinic/', views.createMobileClinic, name='create-mobileclinic'),
    path('update-mobileclinic/<str:pk>', views.updateMobileClinic, name='update-mobileclinic'),
    path('delete-mobileclinic/<str:pk>', views.deleteMobileClinic, name='delete-mobileclinic'),

    path('activity/<str:pk>', views.activity, name='activity'),
    path('create-activity/', views.createActivity, name='create-activity'),
    path('update-activity/<str:pk>', views.updateActivity, name='update-activity'),
    path('delete-activity/<str:pk>', views.deleteActivity, name='delete-activity'),

    path('resource/<str:pk>', views.resource, name='resource'),
    path('create-resource/', views.createResource, name='create-resource'),
    path('update-resource/<str:pk>', views.updateResource, name='update-resource'),
    path('delete-resource/<str:pk>', views.deleteResource, name='delete-resource'),

    path('patient/<str:pk>', views.patient, name='patient'),
    path('create-patient/', views.createPatient, name='create-patient'),
    path('update-patient/<str:pk>', views.updatePatient, name='update-patient'),
    path('delete-patient/<str:pk>', views.deletePatient, name='delete-patient'),
]