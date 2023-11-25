from django.db import migrations

def seed_mobileclinics(apps, schema_editor):
    Mobileclinic = apps.get_model('base', 'Mobileclinic')  # Update 'your_app_name' to your Django app's name

    # Create seed data for the Mobileclinic model
    mobileclinics = [
        {'manager_id': 1, 'name': 'Clinic 1', 'num_of_staff': 10, 'clinic_services': 'Emergency Medical Care', 'clinic_capacity': 50, 'total_annual_budget': 100000, 'pharmaceutical_expenditure': 50000, 'pharmaceutical_waste': 0},
        {'manager_id': 1, 'name': 'Clinic 2', 'num_of_staff': 15, 'clinic_services': 'Infectious Disease Control', 'clinic_capacity': 75, 'total_annual_budget': 150000, 'pharmaceutical_expenditure': 151000, 'pharmaceutical_waste': 1000},
        {'manager_id': 1, 'name': 'Clinic 3', 'num_of_staff': 30, 'clinic_services': 'Wound Care', 'clinic_capacity': 100, 'total_annual_budget': 175000, 'pharmaceutical_expenditure': 200000, 'pharmaceutical_waste': 25000},
        {'manager_id': 1, 'name': 'Clinic 4', 'num_of_staff': 45, 'clinic_services': 'Rescue and Evacuation Support', 'clinic_capacity': 125, 'total_annual_budget': 200000, 'pharmaceutical_expenditure': 75000, 'pharmaceutical_waste': 0},
        {'manager_id': 2, 'name': 'Clinic 5', 'num_of_staff': 70, 'clinic_services': 'Infectious Disease Control', 'clinic_capacity': 150, 'total_annual_budget': 135000, 'pharmaceutical_expenditure': 200000, 'pharmaceutical_waste': 65000},
        {'manager_id': 2, 'name': 'Clinic 6', 'num_of_staff': 10, 'clinic_services': 'Mental Health Support', 'clinic_capacity': 75, 'total_annual_budget': 20000, 'pharmaceutical_expenditure': 75000, 'pharmaceutical_waste': 50000},
        {'manager_id': 2, 'name': 'Clinic 7', 'num_of_staff': 200, 'clinic_services': 'Health Education', 'clinic_capacity': 1200, 'total_annual_budget': 140000, 'pharmaceutical_expenditure': 140000, 'pharmaceutical_waste': 0},
        {'manager_id': 2, 'name': 'Clinic 8', 'num_of_staff': 1000, 'clinic_services': 'Emergency Medical Care', 'clinic_capacity': 5000, 'total_annual_budget': 2000000, 'pharmaceutical_expenditure': 175000, 'pharmaceutical_waste': 0},
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
        {'mobile_clinic': clinics[1], 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-11-30', 'quantity': 50},
        {'mobile_clinic': clinics[1], 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-30', 'quantity': 2000},
        {'mobile_clinic': clinics[2], 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-10-29', 'quantity': 50},
        {'mobile_clinic': clinics[2], 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-15', 'quantity': 2500},
        {'mobile_clinic': clinics[3], 'name': 'Medical Kit', 'type': 'Medical Equipment', 'expiration_date': '2023-11-30', 'quantity': 500},
        {'mobile_clinic': clinics[3], 'name': 'Vaccines', 'type': 'Vaccines and Immunization', 'expiration_date': '2024-06-10', 'quantity': 1000},
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
        {'mobile_clinic': clinics[0], 'date': '2023-10-07', 'latitude': 31.5058, 'longitude': 34.4462, 'population_density': 1500000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 500000, 'weather_status': 'Dust Storm'},
        {'mobile_clinic': clinics[0], 'date': '2021-05-05', 'latitude': 15.4299, 'longitude': 32.5854, 'population_density': 27000, 'crisis_type': 'Financial Crises', 'status': 'inActive', 'num_of_patients': 10000, 'weather_status': 'Rain'},
        {'mobile_clinic': clinics[0], 'date': '2022-11-19', 'latitude': 14.2529, 'longitude': 33.0249, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[1], 'date': '2019-10-25', 'latitude': 13.164806, 'longitude': 30.152973, 'population_density': 2000000, 'crisis_type': 'Healthcare Crises', 'status': 'inActive', 'num_of_patients': 100000, 'weather_status': 'Dust Storm'},
        {'mobile_clinic': clinics[1], 'date': '2023-10-07', 'latitude': 15.474328, 'longitude': 36.358549, 'population_density': 1500000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 500000, 'weather_status': 'Dust Storm'},
        {'mobile_clinic': clinics[1], 'date': '2021-05-05', 'latitude': 11.501019, 'longitude': 42.869273, 'population_density': 27000, 'crisis_type': 'Financial Crises', 'status': 'inActive', 'num_of_patients': 10000, 'weather_status': 'Rain'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 14.056526, 'longitude': 34.106799, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 23.341751, 'longitude': 22.209969, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 31.335443, 'longitude': 34.307786, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 31.542831, 'longitude': 34.508344, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[1], 'date': '2022-11-19', 'latitude': 33.375237, 'longitude': 35.503279, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 32.288265, 'longitude': 35.03354, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 32.204638, 'longitude': 35.283375, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 34.420392, 'longitude': 38.214511, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 32.794144, 'longitude': 36.12424, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 33.463411, 'longitude': 37.610075, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[2], 'date': '2022-11-19', 'latitude': 35.241021, 'longitude': 40.313276, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude': 36.363688, 'longitude': 40.565702, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude': 36.124454, 'longitude': 37.34575, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude': 35.819985, 'longitude': 36.5751, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude': 35.500816, 'longitude': 35.839377, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude': 34.845254, 'longitude': 35.9062, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'inActive', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
        {'mobile_clinic': clinics[3], 'date': '2022-11-19', 'latitude':35.070357, 'longitude': 36.741878, 'population_density': 71000, 'crisis_type': 'Food and Water Contamination', 'status': 'Active', 'num_of_patients': 5000, 'weather_status': 'Heatwave'},
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
        {'Activity': activities[4], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[4], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[5], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[5], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[6], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[6], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[8], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[8], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[7], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[7], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[7], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[9], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[9], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[9], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[10], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[10], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[11], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[11], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[12], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[12], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[13], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[13], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[13], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[14], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[14], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[14], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[15], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[15], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[16], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[16], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[18], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[18], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[17], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[17], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[17], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[19], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[19], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[19], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[20], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[20], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[21], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[21], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
        {'Activity': activities[22], 'age': 15, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[22], 'age': 10, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[23], 'age': 2, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[23], 'age': 20, 'gender': 'Female', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[20], 'age': 70, 'gender': 'Male', 'diagnosis': 'Wound infections', 'medication_date': '2023-10-07'},
        {'Activity': activities[21], 'age': 82, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2023-10-07'},
        {'Activity': activities[22], 'age': 25, 'gender': 'Male', 'diagnosis': 'Fever and cold', 'medication_date': '2022-11-19'},
        {'Activity': activities[23], 'age': 10, 'gender': 'Female', 'diagnosis': 'Minor injuries', 'medication_date': '2022-11-19'},
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