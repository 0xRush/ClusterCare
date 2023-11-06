from ..models import HistoricalActivity, PredictionActivity
from sklearn_som.som import SOM
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def ML_train():
    historical_data = HistoricalActivity.find()
    
    df = pd.DataFrame(historical_data)
    print(df)
    print(df.dtypes)

    columns_for_training = ['num_of_staff', 'clinic_services', 'clinic_capacity', 'total_annual_budget', 'pharmaceutical_expenditure', 'pharmaceutical_waste',
                            'num_of_patients', 'zone', 'date', 'population_density', 'crisis_type', 'age', 'gender', 'diagnosis']

    categorical_columns = ['clinic_services', 'zone', 'date', 'crisis_type', 'gender', 'diagnosis']
    
    encoder = LabelEncoder()
    for column in categorical_columns:
        df[column] = encoder.fit_transform(df[column])
   
    som = SOM(m=3, n=1, dim=len(columns_for_training))  
    som.fit(df[columns_for_training].values)  

    prediction_data = som.predict(df[columns_for_training].values)
    print(prediction_data)

