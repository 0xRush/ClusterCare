from ..models import HistoricalActivity, PredictionActivity

def fetch_historical_data(cluster):
    try:
        historical_data = HistoricalActivity.find({"cluster": int(cluster[0])})
        return historical_data
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

def predection_data(cluster):
    for retry in range(5):  # You can adjust the number of retries as needed
        historical_data = fetch_historical_data(cluster)
        if historical_data is not None:
            break
        
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
        print(data)
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
        print(f"Error in max function: {e}")
        return None

    predected_data = {
        'cluster':int(cluster[0]),
        'age':most_ages,
        'gender':most_gender,
        'diagnosis':most_diag,
        'area':most_area,
        }
    
    PredictionActivity.insert_one(predected_data)

    return predected_data