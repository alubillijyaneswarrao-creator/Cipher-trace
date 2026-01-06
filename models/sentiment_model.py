from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_score(text):
    return analyzer.polarity_scores(text)["compound"]
