import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review and get instant sentiment prediction!")

# Input box
review = st.text_area("Enter your movie review here:", height=150)

# Predict button
if st.button("Analysis Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            # Call your Flask backend
            response = requests.post(
                "https://sentiment-analysis-88p7.onrender.com/predict",
                json={"reviews": review}
            )
            result = response.json()

        # Display result
        sentiment = result['prediction']
        # confidence = result['confidence']
        
        # DEBUG INFO - Remove after testing
        st.write(f"🔍 DEBUG - Raw value: '{sentiment}'")
        st.write(f"🔍 DEBUG - Type: {type(sentiment)}")
        st.write(f"🔍 DEBUG - Lowercase: '{str(sentiment).lower()}'")

        sentiment_lower = str(sentiment).lower()
        
        # Fixed: Check for "positive" or "pos" only if it's the main sentiment
        if "positive" in sentiment_lower or sentiment_lower == "pos":
            st.success(f"✅ Sentiment : {sentiment}")
        elif "negative" in sentiment_lower or sentiment_lower == "neg":
            st.error(f"❌ Sentiment : {sentiment}")
        else:
            st.info(f"ℹ️ Sentiment : {sentiment}")

        # st.metric(Label="Confidence", value=confidence)
