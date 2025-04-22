import json
import joblib
import os

# Load model at start-up
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def lambda_handler(event, context):
    try:
        input_value = event.get('queryStringParameters', {}).get('input', None)
        if input_value is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing input parameter.')
            }
        
        input_value = float(input_value)
        prediction = model.predict([[input_value]])
        
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': prediction.tolist()})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
