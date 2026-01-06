from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Minimal training data (demo-safe)
TRAIN_DATA = [
    "I hate you",
    "You are stupid",
    "Go die",
    "You are amazing",
    "Thank you so much",
    "Have a nice day"
]

LABELS = [1, 1, 1, 0, 0, 0]  # 1 = harassment, 0 = clean

# Train at startup
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(TRAIN_DATA)

model = LogisticRegression()
model.fit(X, LABELS)

def predict_comment(text: str) -> float:
    vec = vectorizer.transform([text])
    return model.predict_proba(vec)[0][1]
