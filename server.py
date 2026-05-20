from fastapi import FastAPI
import joblib
import numpy as np

model1 = joblib.load('app/binary_classification.joblib')
model2 = joblib.load('app/multiclass_classification.joblib')

class_names_1 = np.array(['Not an attack', 'Attack'])
class_names_2 = np.array(['Dos attacks', 'Probe attacks', 'Privilege attacks', 'Access attacks'])

app = FastAPI()

@app.get('/')
def reed_root():
    return {'message' : 'Attack Detection Model API'}

@app.post('/predict')
def predict(data:dict):
    features = np.array(data['features']).reshape(1,-1)
    prediction = model1.predict(features)
    class_name_1 = class_names_1[prediction][0]

    if class_name_1 == class_names_1[0]:
        class_name_2 == class_name_1
    else:
        prediction_2 = model2.predict(features)
        class_name_2 = class_names_2[prediction_2][0]    
    return {'predicted flag': class_name_1,
            'predicted class': class_name_2}



