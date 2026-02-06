
import re

def extract_fields(text):
    patterns = {
        "policyNumber": r"Policy Number:\s*(.*)",
        "policyholderName": r"Policyholder Name:\s*(.*)",
        "incidentDate": r"Incident Date:\s*(.*)",
        "incidentTime": r"Incident Time:\s*(.*)",
        "location": r"Location:\s*(.*)",
        "description": r"Description:\s*(.*)",
        "claimType": r"Claim Type:\s*(.*)",
        "estimatedDamage": r"Estimated Damage:\s*(\d+)",
        "attachments": r"Attachments:\s*(.*)",
        "initialEstimate": r"Initial Estimate:\s*(\d+)"
    }
    extracted = {}
    for k, p in patterns.items():
        m = re.search(p, text)
        extracted[k] = m.group(1) if m else None
    if extracted.get("estimatedDamage"):
        extracted["estimatedDamage"] = int(extracted["estimatedDamage"])
    return extracted
