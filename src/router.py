
MANDATORY_FIELDS = ["policyNumber","incidentDate","description","claimType","estimatedDamage"]
SUSPICIOUS_KEYWORDS = ["fraud","staged","inconsistent"]

def route_claim(fields):
    missing = [f for f in MANDATORY_FIELDS if not fields.get(f)]
    desc = (fields.get("description") or "").lower()
    if any(w in desc for w in SUSPICIOUS_KEYWORDS):
        return "Investigation Flag", missing, "Suspicious keywords detected."
    if missing:
        return "Manual Review", missing, "Mandatory fields missing."
    if fields.get("claimType","").lower() == "injury":
        return "Specialist Queue", missing, "Injury related claim."
    if fields.get("estimatedDamage",0) < 25000:
        return "Fast-track", missing, "Low damage amount."
    return "Manual Review", missing, "High value claim."
