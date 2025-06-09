

import spacy
import re
from typing import Dict

# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

def parse_test_case(description: str) -> Dict:
    """
    Parse a plain English test case description into structured JSON-like data.
    """
    doc = nlp(description)
    
    # Initialize fields
    action = ""
    obj = ""
    expected_result = ""

    # Find first verb as the action
    for token in doc:
        if token.pos_ == "VERB":
            action = token.lemma_
            break

    # Find the first noun phrase as the object
    for chunk in doc.noun_chunks:
        if chunk.root.dep_ in ("dobj", "pobj", "nsubj"):
            obj = chunk.text
            break

    # Use regex to find expected result phrases
    expected_match = re.search(r"(should|must|expected to|expected result is|will|then).*", description, re.IGNORECASE)
    if expected_match:
        expected_result = expected_match.group(0).strip()

    # Fallback if no explicit expected result found
    if not expected_result:
        expected_result = "Not explicitly mentioned"

    return {
        "description": description,
        "action": action.capitalize() if action else "Unknown",
        "object": obj.capitalize() if obj else "Unknown",
        "expected_result": expected_result
    }
