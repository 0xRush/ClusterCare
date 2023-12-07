from ..models import HistoricalActivity, PredictionActivity, Mobileclinic
from .seeding_DB import get_coordinates
from .ML_tst import change_data, testML

def predection_data(cluster):
    historical_data = HistoricalActivity.find({"cluster": int(cluster[0])})
        
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
        diagnosis[data['diagnosis']] = diagnosis.get(data['diagnosis'], 0) + 1
        zone[data['zone']] = zone.get(data['zone'], 0) + 1
    
    try:
        most_ages = max(ages, key=lambda k: ages[k])
        most_gender = max(gender, key=lambda k: gender[k])
        most_diag = max(diagnosis, key=lambda k: diagnosis[k])
        most_area = max(zone, key=lambda k: zone[k])
    except Exception as e:
        print(f"Cluster not found: {e}")
        return None

    predected_data = {
        'cluster':int(cluster[0]),
        'age':most_ages,
        'gender':most_gender,
        'diagnosis':most_diag,
        'area': get_coordinates(most_area),
    }

    predection = PredictionActivity.find_one({"cluster": int(cluster[0])})
    
    if predection:
        updated_data = {
        '$set': {
            'age': most_ages,
            'gender': most_gender,
            'diagnosis': most_diag,
            'area': get_coordinates(most_area),
            }
        }

        PredictionActivity.update_one({'cluster': int(cluster[0])}, updated_data)
    else:
        PredictionActivity.insert_one(predected_data)


def ML_predict():
    mobileclinic = Mobileclinic.objects.get(id=8)
    data = change_data(mobileclinic)
    test = testML(data)
    predection_data(test)