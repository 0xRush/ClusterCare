from ..models import HistoricalActivity
from sklearn_som.som import SOM
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import joblib

def trainML():
    historical_data = HistoricalActivity.find()
    
    df = pd.DataFrame(historical_data)
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

    som = SOM(m=3, n=1, dim=len(columns_for_training))  
    som.fit(newData)  

    prediction_data = som.predict(newData)

    for idx, cluster in enumerate(prediction_data):
        oid = df['_id'][idx]  
        HistoricalActivity.update_one({"_id": oid}, {"$set": {"cluster": int(cluster)}})
    
    joblib.dump(som, 'model.joblib')
