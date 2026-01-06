THREAT_KEYWORDS = [
    "kill", "stab", "shoot", "bomb", "attack", "you will regret"
]

def threat_detection(text):
    text = text.lower()
    for word in THREAT_KEYWORDS:
        if word in text:
            return {"threat": True, "confidence": "HIGH"}
    return {"threat": False, "confidence": "LOW"}
