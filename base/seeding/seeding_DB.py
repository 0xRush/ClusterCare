from ..models import Mobileclinic, Activity, Patient, HistoricalActivity, PredictionActivity
from django.shortcuts import get_list_or_404
import datetime
from geopy.geocoders import Nominatim


# this is a solution by using request library
# import requests

# def get_country(lat, lon):
#     url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&zoom=3'
#     try:
#         result = requests.get(url=url)
#         result_json = result.json()
#         return result_json['display_name']
#     except:
#         return None

def get_city_name(latitude, longitude):
    geolocator = Nominatim(user_agent="test_app")
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

    return city

# for the first time
def seed():
    mobileclinics = get_list_or_404(Mobileclinic)

    for mobileclinic in mobileclinics:
        activities = Activity.objects.filter(mobile_clinic=mobileclinic)
        
        if activities is not None:
            for activity in activities:
                patients = Patient.objects.filter(Activity=activity)
                zone = get_city_name(activity.latitude, activity.longitude)
                
                if patients is not None:
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

#  for prediction
# zone
# Age
# diagnosis_percentage 