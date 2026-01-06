from models.harassment_model import predict_comment
from models.sentiment_model import sentiment_score
from models.threat_model import threat_detection

def severity_label(harassment_prob, sentiment):
    # Strong positive sentiment override
    if sentiment >= 0.4:
        return "LOW"

    # Clear non-harassment
    if harassment_prob < 0.3:
        return "LOW"

    # Uncertain / borderline
    if harassment_prob < 0.6:
        return "MEDIUM"

    # Clear harassment
    return "HIGH"


def full_analysis(text: str):
    harassment_prob = predict_comment(text)
    sentiment = sentiment_score(text)
    threat_result = threat_detection(text)

    analysis = {
        "harassment_prob": harassment_prob,
        "sentiment": sentiment,
        "severity": severity_label(harassment_prob, sentiment),
        "threat": threat_result["threat"],
        "threat_confidence": threat_result["confidence"]
    }

    return analysis

