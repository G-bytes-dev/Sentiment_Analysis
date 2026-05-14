import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_URL = os.getenv("API_URL", "https://sentiment-analysis-88p7.onrender.com/predict")
API_TIMEOUT = 10
MAX_REVIEW_LENGTH = 5000

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
if st.button("Analyze Sentiment", type="primary"):
    review_stripped = review.strip()
    
    # Input validation
    if not review_stripped:
        st.warning("⚠️ Please enter a review first!")
    elif len(review_stripped) > MAX_REVIEW_LENGTH:
        st.error(f"❌ Review exceeds maximum length of {MAX_REVIEW_LENGTH} characters!")
    else:
        with st.spinner("🔄 Analyzing your review..."):
            try:
                # Call Flask backend
                response = requests.post(
                    API_URL,
                    json={"reviews": review_stripped},
                    timeout=API_TIMEOUT
                )
                response.raise_for_status()  # Raise error for bad status codes
                result = response.json()
                
                # Validate response structure
                if "prediction" not in result:
                    st.error("❌ Invalid response from server. Missing 'prediction' field.")
                else:
                    # Display result
                    sentiment = str(result["prediction"]).lower().strip()
                    confidence = result.get("confidence", "N/A")
                    
                    # Determine sentiment type
                    if sentiment in ["positive", "pos"]:
                        st.success(f"✅ **Sentiment:** Positive")
                        st.balloons()
                    elif sentiment in ["negative", "neg"]:
                        st.error(f"❌ **Sentiment:** Negative")
                    elif sentiment in ["neutral", "neutral_"]:
                        st.info(f"ℹ️ **Sentiment:** Neutral")
                    else:
                        st.warning(f"⚠️ **Sentiment:** Unknown ({sentiment})")
                    
                    # Display confidence if available
                    if confidence != "N/A":
                        st.metric("Confidence Score", f"{confidence}%")
                    
                    # Show analyzed review
                    with st.expander("📖 Your Review"):
                        st.text(review_stripped)
                        
            except requests.exceptions.Timeout:
                st.error("❌ Request timeout. The API took too long to respond. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("❌ Connection error. Unable to reach the API. Please check your internet connection.")
            except requests.exceptions.HTTPError as e:
                st.error(f"❌ API error: {e.response.status_code} - {e.response.reason}")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Request failed: {str(e)}")
            except ValueError:
                st.error("❌ Failed to parse API response. Please try again.")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
