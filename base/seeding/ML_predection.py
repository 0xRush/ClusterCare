from ..models import HistoricalActivity, PredictionActivity
import time

def predection_data(cluster):
    historical_data = HistoricalActivity.find({"cluster": int(cluster[0])})
    # zone
    # age
    # percentage of diag
    ages = {
        'Child': 0,
        'Young': 0,
        'Middle_aged': 0,
        'Old_aged': 0,
    }
    gender = {
        'Male': 0,
        'Female': 0
    }
    zone = {}
    diagnosis = {}

    for data in historical_data:
        ages['Old_aged'] += data['Old_aged']
        ages['Middle_aged'] += data['Middle_aged']
        ages['Young'] += data['Young']
        ages['Child'] += data['Child']
        gender['Male'] += data['Male']
        gender['Female'] += data['Female']
        if data['diagnosis'] in diagnosis.keys():
            diagnosis[data['diagnosis']] += 1
        else:
            diagnosis[data['diagnosis']] = 1

        if data['zone'] in zone.keys():
            zone[data['zone']] += 1
        else:
            zone[data['zone']] = 1

    time.sleep(7)
    
    most_ages = max(ages, key=lambda k: ages[k])
    most_gender = max(gender, key=lambda k: gender[k])
    most_diag = max(diagnosis, key=lambda k: diagnosis[k])
    most_area = max(zone, key=lambda k: zone[k])

    predected_data = {
        'cluster':int(cluster[0]),
        'age':most_ages,
        'gender':most_gender,
        'diagnosis':most_diag,
        'area':most_area,
        }
    
    PredictionActivity.insert_one(predected_data)

    return predected_data