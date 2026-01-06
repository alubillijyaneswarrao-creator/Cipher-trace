from models.harassment_model import predict_comment
from models.sentiment_model import sentiment_score
from models.threat_model import threat_detection

def severity_label(score):
    if score > 0.7:
        return "HIGH"
    elif score > 0.4:
        return "MEDIUM"
    return "LOW"

def full_analysis(text):
    threat_result = threat_detection(text)

    analysis = {
        "harassment_prob": predict_comment(text),
        "sentiment": sentiment_score(text),
        "severity": "HIGH",  # simplified here
        "threat": threat_result["threat"],
        "threat_confidence": threat_result["confidence"]
    }

    return analysis
