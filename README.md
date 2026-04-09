# 🎬 Sentiment Analysis Web App

A **Machine Learning–powered Sentiment Analysis application** that predicts whether a movie review expresses **positive or negative sentiment**.  

The project combines **Natural Language Processing (NLP)**, a **Flask API**, and a **Streamlit web interface** to create a complete **end-to-end ML application**.  

Users can enter a movie review, and the system processes the text, extracts features, and predicts the sentiment instantly.

---

## 🚀 Demo

### Example Input
```
This movie was absolutely amazing and the acting was fantastic!
```

### Example Output
```
Sentiment: Positive
```


## 🧠 How It Works

### 1️⃣ Text Preprocessing
- Convert text to lowercase  
- Remove punctuation and numbers  
- Tokenization  
- Stopword removal  
- Lemmatization  

### 2️⃣ Feature Extraction
Convert text into numerical features using **TF-IDF Vectorization**.

### 3️⃣ Prediction
A trained **Machine Learning model** predicts the sentiment of the review.

### 4️⃣ Deployment
- Flask API handles prediction requests  
- Streamlit UI provides an interactive web interface

## 🏗 Project Architecture

```
User
  │
  ▼
Streamlit Web App
  │
  ▼
Flask API (/predict)
  │
  ▼
Text Preprocessing (NLTK)
  │
  ▼
TF-IDF Vectorizer
  │
  ▼
Machine Learning Model
  │
  ▼
Sentiment Prediction
```

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- NLTK  
- Flask  
- Streamlit  
- Joblib  
- Requests

## 📂 Project Structure

```
sentiment_analysis/
│
├── app.py              # Flask API
├── preprocess.py       # Text preprocessing functions
├── streamlit_app.py    # Streamlit UI
├── model.joblib        # Trained ML model
├── tf_idf.joblib       # TF-IDF vectorizer
├── nltk.ipynb          # Model training notebook
├── requirements.txt    # Project dependencies
└── README.md
```


## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/sentiment-analysis.git
cd sentiment-analysis
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Flask API

```
python app.py
```

### 4️⃣ Run the Streamlit App

```
streamlit run streamlit_app.py
```

## 📡 API Endpoint

### Predict Sentiment

**POST /predict**

### Example Request
```json
{
  "reviews": "This movie is amazing!"
}
```

### Example Response
```json
{
  "prediction": "positive"
}
```


## ✨ Features

- ✅ NLP text preprocessing  
- ✅ TF-IDF feature extraction  
- ✅ Machine learning sentiment prediction  
- ✅ Flask REST API  
- ✅ Interactive Streamlit interface
  
## 📌 Future Improvements

- Add confidence score  
- Support multiple reviews at once  
- Deploy using Docker  
- Add deep learning models (LSTM / BERT)
