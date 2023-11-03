from django.db import migrations

def seed_mobileclinics(apps, schema_editor):
    Mobileclinic = apps.get_model('base', 'Mobileclinic')  # Update 'your_app_name' to your Django app's name

    # Create seed data for the Mobileclinic model
    mobileclinics = [
        {'manager_id': 1, 'name': 'Clinic 1', 'num_of_staff': 10, 'clinic_services': 'Emergency Medical Care', 'clinic_capacity': 50, 'total_annual_budget': 100000, 'pharmaceutical_expenditure': 50000, 'pharmaceutical_waste': 1000},
        {'manager_id': 2, 'name': 'Clinic 2', 'num_of_staff': 15, 'clinic_services': 'Wound Care', 'clinic_capacity': 75, 'total_annual_budget': 150000, 'pharmaceutical_expenditure': 75000, 'pharmaceutical_waste': 2000},
        # Add more mobile clinic data as needed
    ]

    for clinic_data in mobileclinics:
        Mobileclinic.objects.create(**clinic_data)

def seed_resources(apps, schema_editor):
    Resources = apps.get_model('your_app_name', 'Resources')  # Update 'your_app_name' to your Django app's name

    # Create seed data for the Resources model related to a specific mobile clinic
    resources = [
        {'mobile_clinic_id': 1, 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-12-31', 'quantity': 100},
        {'mobile_clinic_id': 2, 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-30', 'quantity': 5000},
        # Add more resources data as needed
    ]

    for resource_data in resources:
        Resources.objects.create(**resource_data)

def seed_activities(apps, schema_editor):
    Activity = apps.get_model('your_app_name', 'Activity')

    activities = [
        {'mobile_clinic_id': 1, 'date': '2023-11-03', 'latitude': 40.7128, 'longitude': -74.0060, 'population_density': 1000, 'crisis_type': 'Earthquakes', 'status': 'Active', 'num_of_patients': 50, 'weather_status': 'Clear Sky'},
        {'mobile_clinic_id': 2, 'date': '2023-11-04', 'latitude': 34.0522, 'longitude': -118.2437, 'population_density': 800, 'crisis_type': 'Wildfires', 'status': 'Active', 'num_of_patients': 30, 'weather_status': 'Partly Cloudy'},
        # Add more activity data as needed
    ]

    for activity_data in activities:
        Activity.objects.create(**activity_data)

def seed_patients(apps, schema_editor):
    Patient = apps.get_model('your_app_name', 'Patient')

    patients = [
        {'activity_id': 1, 'age': 35, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2023-11-03'},
        {'activity_id': 2, 'age': 45, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-11-04'},
        # Add more patient data as needed
    ]

    for patient_data in patients:
        Patient.objects.create(**patient_data)

class Migration(migrations.Migration):
    dependencies = [
        ('base', None),  # Replace with your app and the previous migration number for Mobileclinic
    ]

    operations = [
        migrations.RunPython(seed_mobileclinics),
        migrations.RunPython(seed_resources),
        migrations.RunPython(seed_activities),
        migrations.RunPython(seed_patients),
    ]
