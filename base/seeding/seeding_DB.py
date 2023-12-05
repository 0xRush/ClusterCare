from ..models import Mobileclinic, Activity, Patient, HistoricalActivity, PredictionActivity
from django.shortcuts import get_list_or_404
<<<<<<< HEAD
=======
import datetime
from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_app")
    location = geolocator.geocode(city_name)

    # Check if location is found
    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude
    else:
        return None

def get_city_name(latitude, longitude):
    geolocator = Nominatim(user_agent="city_app")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    address = location.raw['address']
    
    # Try to get the city from the address information
    city = address.get('city', '')
    
    # If city is not available, try other alternatives such as town, village, or other naming conventions
    if not city:
        city = address.get('town', '')
        if not city:
            city = address.get('village', '')
            if not city:
                city = address.get('other_name', '')
                if not city:
                    city = None
                    
    return city
>>>>>>> 5f17f85f940cf9521e64006fb6eaec586744fb24

<<<<<<< HEAD

=======
# for the first time
>>>>>>> Iyas
def seed():
    mobileclinics = get_list_or_404(Mobileclinic)

    for mobileclinic in mobileclinics:
        activities = Activity.objects.filter(mobile_clinic=mobileclinic)
        
<<<<<<< HEAD
        for activity in activities:
            patients = Patient.objects.filter(Activity=activity)
            zone = [activity.latitude, activity.longitude]
            
            for patient in patients:
                HistoricalActivity.insert_one(
                    {
                    # we need AVg annual disaster and weather fluctuations
                        # from mobile clinic
                        'num_of_staff': mobileclinic.num_of_staff,
                        'clinic_services': mobileclinic.clinic_services,
                        'clinic_capacity': mobileclinic.clinic_capacity,
                        'total_annual_budget': mobileclinic.total_annual_budget,
                        'pharmaceutical_expenditure': mobileclinic.pharmaceutical_expenditure,
                        'pharmaceutical_waste': mobileclinic.pharmaceutical_waste,
                        # from activity
                        'num_of_patients': activity.num_of_patients,
                        'zone': zone,
                        'date': f'{activity.date}',
                        'population_density': activity.population_density,
                        'crisis_type': activity.crisis_type,
                        # from patient
                        'age': patient.age,
                        'gender': patient.gender,
                        'diagnosis': patient.diagnosis,
                    }
                )
    print('seeding..')

=======
        if activities is not None:
            for activity in activities:
                patients = Patient.objects.filter(Activity=activity)
                zone = get_city_name(activity.latitude, activity.longitude)
                
                info = {
                    'Child':0,
                    'Young':0,
                    'Middle_aged':0,
                    'Old_aged':0,
                    'Male':0,
                    'Female':0,  
                }

                diagnosis = {
                    'E11':0,
                    'I10':0,
                    'F32':0,
                    'J20':0,
                    'I10':0,
                    'M17':0,
                    'I21':0,
                    'J45':0,
                    'N39.0':0,
                    'M47.812':0,
                }
                if patients is not None:
                    for patient in patients:
                        if patient.age > 45:
                            info['Old_aged'] += 1
                        elif patient.age > 30:
                            info['Middle_aged'] += 1
                        elif patient.age > 16:
                            info['Young'] += 1
                        else:
                            info['Child'] += 1

                        info[patient.gender] += 1

                        diagnosis[patient.diagnosis] += 1 

                    most_diag = max(diagnosis, key=lambda k: diagnosis[k])
                       
                    HistoricalActivity.insert_one(
                        {
                        # we need AVg annual disaster and weather fluctuations
                            # from mobile clinic
                            'num_of_staff': mobileclinic.num_of_staff,
                            'clinic_services': mobileclinic.clinic_services,
                            'clinic_capacity': mobileclinic.clinic_capacity,
                            'total_annual_budget': mobileclinic.total_annual_budget,
                            'pharmaceutical_expenditure': mobileclinic.pharmaceutical_expenditure,
                            'pharmaceutical_waste': mobileclinic.pharmaceutical_waste,
                            # from activity
                            'num_of_patients': activity.num_of_patients,
                            'zone': zone,
                            'date': f'{activity.date}',
                            'population_density': activity.population_density,
                            'crisis_type': activity.crisis_type,
                            # from patient
                            'Male': info['Male'],
                            'Female': info['Female'],
                            'Child': info['Child'],
                            'Young': info['Young'],
                            'Middle_aged': info['Middle_aged'],
                            'Old_aged': info['Old_aged'],
                            'diagnosis': most_diag,
                        }
                    )
    print('seeding..')

# the rest
# def seed():
#     mobileclinics = get_list_or_404(Mobileclinic)

#     for mobileclinic in mobileclinics:
#         activities = Activity.objects.filter(mobile_clinic=mobileclinic)
        
#         if activities is not None:
#             for activity in activities:
#                 if activity.date == datetime.date.today():
#                     patients = Patient.objects.filter(Activity=activity)
#                     zone = [activity.latitude, activity.longitude]
                    
#                     if patients is not None:
#                         for patient in patients:
#                             HistoricalActivity.insert_one(
#                                 {
#                                 # we need AVg annual disaster and weather fluctuations
#                                     # from mobile clinic
#                                     'num_of_staff': mobileclinic.num_of_staff,
#                                     'clinic_services': mobileclinic.clinic_services,
#                                     'clinic_capacity': mobileclinic.clinic_capacity,
#                                     'total_annual_budget': mobileclinic.total_annual_budget,
#                                     'pharmaceutical_expenditure': mobileclinic.pharmaceutical_expenditure,
#                                     'pharmaceutical_waste': mobileclinic.pharmaceutical_waste,
#                                     # from activity
#                                     'num_of_patients': activity.num_of_patients,
#                                     'zone': zone,
#                                     'date': f'{activity.date}',
#                                     'population_density': activity.population_density,
#                                     'crisis_type': activity.crisis_type,
#                                     # from patient
#                                     'age': patient.age,
#                                     'gender': patient.gender,
#                                     'diagnosis': patient.diagnosis,
#                                 }
#                             )
#     print('seeding..')
>>>>>>> Iyas

#  for prediction
# zone
# Age
# diagnosis_percentage 