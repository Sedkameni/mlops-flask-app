import numpy as np
import joblib

def load_model(model_path="model.joblib"):
     """Load the pre-trained ML model"""
     model = joblib.load(model_path)
     return model

def predict(weight):
     """Make a prediction based on the input weight"""
     model = load_model()
     prediction = model.predict([[weight]])
     height_inches = prediction[0]
     height_human_readable = convert_inches_to_feet(height_inches)
     return {"height_inches": height_inches, "height_human_readable": height_human_readable}

def convert_inches_to_feet(inches):
     feet = int(inches // 12)
     remaining_inches = int(inches % 12)
     return f"{feet} foot, {remaining_inches} inches"