from flask import Flask, request, jsonify
import mlib

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
     """Predicts the Height of MLB Players"""
     json_payload = request.json
     prediction = mlib.predict(json_payload['Weight'])
     return jsonify({'prediction': prediction, 'status': 'success'})

@app.route("/")
def home():
     return "<h3>MLPops Flask ML Service</h3>"

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8080, debug=True)