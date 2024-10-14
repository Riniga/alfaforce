
import re

def contains_word(text, word):
    pattern = rf'\b{re.escape(word)}[\s,.?!]*([A-Za-z0-9].*)'
    match = re.search(pattern, text, re.IGNORECASE)
    if match: return  match.group(1).strip()

    return None