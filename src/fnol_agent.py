
import json
from extractor import extract_fields
from router import route_claim

def process_fnol(text):
    fields = extract_fields(text)
    route, missing, reason = route_claim(fields)
    return {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

if __name__ == "__main__":
    with open("../data/sample_fnol.txt") as f:
        text = f.read()
    result = process_fnol(text)
    print(json.dumps(result, indent=2))
