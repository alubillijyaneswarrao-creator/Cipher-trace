def admin_decision_engine(analysis):
    if analysis["threat"]:
        return {"decision": "ESCALATE", "reason": "Threat detected"}

    if analysis["severity"] == "HIGH":
        return {"decision": "TEMP_BLOCK", "reason": "Severe harassment"}

    if analysis["severity"] == "MEDIUM":
        return {"decision": "WARN", "reason": "Potential harassment"}

    return {"decision": "ALLOW", "reason": "Benign content"}
