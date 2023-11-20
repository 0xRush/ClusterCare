from sklearn_som.som import SOM
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import joblib
from .seeding_DB import get_city_name
from ..models import Activity, Patient

def change_data(mobileclinic):
    activities = Activity.objects.filter(mobile_clinic=mobileclinic)
    for activity in activities:
        patients = Patient.objects.filter(Activity=activity)
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

        test_data = {
                'num_of_staff': mobileclinic.num_of_staff,
                'clinic_services': mobileclinic.clinic_services,
                'clinic_capacity': mobileclinic.clinic_capacity,
                'total_annual_budget': mobileclinic.total_annual_budget,
                'pharmaceutical_expenditure': mobileclinic.pharmaceutical_expenditure,
                'pharmaceutical_waste': mobileclinic.pharmaceutical_waste,
                'num_of_patients': activity.num_of_patients,
                'zone': '',
                'date': f'{activity.date}',
                'population_density': activity.population_density,
                'crisis_type': activity.crisis_type,
                'Male': info['Male'],
                'Female': info['Female'],
                'Child': info['Child'],
                'Young': info['Young'],
                'Middle_aged': info['Middle_aged'],
                'Old_aged': info['Old_aged'],
                'diagnosis': most_diag,
        }
    return test_data

def testML(test_data):
    df = pd.DataFrame([test_data], index=[0])
    print(df)
    print(df.dtypes)

    columns_for_training = ['num_of_staff', 'clinic_services', 'clinic_capacity', 'total_annual_budget', 'pharmaceutical_expenditure', 'pharmaceutical_waste',
                            'num_of_patients', 'zone', 'date', 'population_density', 'crisis_type', 'Male', 'Female', 'Child', 'Young', 'Middle_aged', 'Old_aged', 'diagnosis']

    categorical_columns = ['clinic_services', 'zone', 'date', 'crisis_type', 'diagnosis']
    
    encoder = LabelEncoder()
    for column in categorical_columns:
        df[column] = encoder.fit_transform(df[column])

    scaler = MinMaxScaler()
    newData = scaler.fit_transform(np.float32(df[columns_for_training].values))

    som = joblib.load('model.joblib')
    som = SOM(m=3, n=1, dim=len(columns_for_training))  
    som.fit(newData)  

    prediction_data = som.predict(newData)

    return prediction_data
