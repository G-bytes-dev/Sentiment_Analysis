import re
import nltk

# Download required datasets
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('English'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize: convert it back to root word
    tokens  = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back to string
    return " ".join(tokens)

print(preprocess("This the best worst movie ever !!"))
