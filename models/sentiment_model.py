import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure VADER lexicon is available (safe to call multiple times)
nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()

def sentiment_score(text: str) -> float:
    return analyzer.polarity_scores(text)["compound"]
