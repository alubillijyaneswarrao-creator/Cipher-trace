import pickle

with open("harassment_ai/trained_models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("harassment_ai/trained_models/harassment_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_comment(text):
    vec = vectorizer.transform([text])
    return model.predict_proba(vec)[0][1]
