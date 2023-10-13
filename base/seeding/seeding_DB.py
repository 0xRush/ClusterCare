from ..models import Mobileclinic, Activity, Patient, HistoricalActivity, PredictionActivity
from django.shortcuts import get_list_or_404

<<<<<<< HEAD

=======
# for the first time
<<<<<<< HEAD
>>>>>>> c637c6ad139a971ed59abd83bb47383ef654b11a
=======
>>>>>>> Iyas
>>>>>>> 4c169ec0186478dc2da8898160a479ff9f6a5815
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
                zone = [activity.latitude, activity.longitude]
                
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
<<<<<<< HEAD
>>>>>>> c637c6ad139a971ed59abd83bb47383ef654b11a
=======
>>>>>>> Iyas
>>>>>>> 4c169ec0186478dc2da8898160a479ff9f6a5815

#  for prediction
# zone
# Age
# diagnosis_percentage 