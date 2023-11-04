from django.db import migrations

def seed_mobileclinics(apps, schema_editor):
    Mobileclinic = apps.get_model('base', 'Mobileclinic')  # Update 'your_app_name' to your Django app's name

    # Create seed data for the Mobileclinic model
    mobileclinics = [
        {'manager_id': 1, 'name': 'Clinic 1', 'num_of_staff': 10, 'clinic_services': 'Emergency Medical Care', 'clinic_capacity': 50, 'total_annual_budget': 100000, 'pharmaceutical_expenditure': 50000, 'pharmaceutical_waste': 0},
        {'manager_id': 1, 'name': 'Clinic 2', 'num_of_staff': 15, 'clinic_services': 'Infectious Disease Control', 'clinic_capacity': 75, 'total_annual_budget': 150000, 'pharmaceutical_expenditure': 151000, 'pharmaceutical_waste': 1000},
        {'manager_id': 2, 'name': 'Clinic 3', 'num_of_staff': 30, 'clinic_services': 'Wound Care', 'clinic_capacity': 100, 'total_annual_budget': 175000, 'pharmaceutical_expenditure': 200000, 'pharmaceutical_waste': 25000},
        {'manager_id': 2, 'name': 'Clinic 4', 'num_of_staff': 45, 'clinic_services': 'Rescue and Evacuation Support', 'clinic_capacity': 125, 'total_annual_budget': 200000, 'pharmaceutical_expenditure': 75000, 'pharmaceutical_waste': 0},
        # Add more mobile clinic data as needed
    ]

    for clinic_data in mobileclinics:
        Mobileclinic.objects.create(**clinic_data)

def seed_resources(apps, schema_editor):
    Resources = apps.get_model('base', 'Resources')  # Update 'your_app_name' to your Django app's name
    Mobileclinic = apps.get_model('base', 'Mobileclinic')

    clinics = Mobileclinic.objects.all()

    # Create seed data for the Resources model related to a specific mobile clinic
    resources = [
        {'mobile_clinic': clinics[0], 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-12-31', 'quantity': 100},
        {'mobile_clinic': clinics[0], 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-30', 'quantity': 5000},
        {'mobile_clinic': clinics[1], 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-12-31', 'quantity': 50},
        {'mobile_clinic': clinics[1], 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-30', 'quantity': 2000},
        # Add more resources data as needed
    ]

    for resource_data in resources:
        Resources.objects.create(**resource_data)

def seed_activities(apps, schema_editor):
    Activity = apps.get_model('base', 'Activity')
    Mobileclinic = apps.get_model('base', 'Mobileclinic')

    clinics = Mobileclinic.objects.all()

    activities = [
        {'mobile_clinic': clinics[0], 'date': '2019-10-25', 'latitude': 31.5134, 'longitude': 34.4554, 'population_density': 2000000, 'crisis_type': 'Healthcare Crises', 'status': 'inActive', 'num_of_patients': 100000, 'weather_status': 'Dust Storm'},
        {'mobile_clinic': clinics[0], 'date': '2023-10-07', 'latitude': 31.5058, 'longitude': 34.4462, 'population_density': 1500000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 500000, 'weather_status': 'Dust Storm'},
        {'mobile_clinic': clinics[1], 'date': '2021-05-05', 'latitude': 15.4299, 'longitude': 32.5854, 'population_density': 27000, 'crisis_type': 'Financial Crises', 'status': 'inActive', 'num_of_patients': 10000, 'weather_status': 'Rain'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 14.2529, 'longitude': 33.0249, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        # Add more activity data as needed
    ]

    for activity_data in activities:
        Activity.objects.create(**activity_data)

def seed_patients(apps, schema_editor):
    Patient = apps.get_model('base', 'Patient')
    Activity = apps.get_model('base', 'Activity')

    activities = Activity.objects.all()

    patients = [
        {'Activity': activities[1], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[1], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[1], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[1], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[1], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[1], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[3], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[3], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        # Add more patient data as needed
    ]

    for patient_data in patients:
        Patient.objects.create(**patient_data)

class Migration(migrations.Migration):
    dependencies = [
        ('base', '0001_initial'),  # Replace with your app and the previous migration number for Mobileclinic
    ]

    operations = [
        migrations.RunPython(seed_mobileclinics),
        migrations.RunPython(seed_resources),
        migrations.RunPython(seed_activities),
        migrations.RunPython(seed_patients),
    ]