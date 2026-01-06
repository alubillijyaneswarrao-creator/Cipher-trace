def admin_decision_engine(analysis):
    if analysis["threat"] and analysis["threat_confidence"] == "HIGH":
        return {"decision": "ESCALATE", "reason": "Threat detected"}

    if analysis["severity"] == "HIGH":
        return {"decision": "TEMP_BLOCK", "reason": "Severe harassment"}

    if analysis["severity"] == "MEDIUM":
        return {"decision": "WARN", "reason": "Moderate harassment"}

    return {"decision": "ALLOW", "reason": "Safe content"}
