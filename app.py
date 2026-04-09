import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# LOADING SAVED MODEL
model = joblib.load('model.joblib')

# LOADING SAVED TF-IDF VECTORIZER
vectorizer = joblib.load('tf_idf.joblib')


# HOME ROUTE (Fix for 404)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Sentiment Analysis API is running!',
        'endpoints': {
            'health': 'GET /health',
            'predict': 'POST /predict'
        }
    })
#def home():
    #return "Sentiment Analysis API is running 🚀"


@app.route("/predict", methods=['POST'])
def predict():

    # READING THE INCOMING JSON DATA
    data = request.get_json()

    # EXTRACT THE FEATURE VALUES FROM MESSAGE
    reviews = data['reviews']

    # PREPROCESS THE REVIEW
    process_review = preprocess(reviews)

    # EXTRACT FEATURES
    process_review = vectorizer.transform([process_review])

    # PREDICT SENTIMENT
    prediction = model.predict(process_review)

    # OUTPUT SENTIMENT
    return jsonify({"prediction": str(prediction[0])})


# HEALTH CHECK
@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
