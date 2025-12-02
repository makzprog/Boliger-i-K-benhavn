import re

def fix_duplicate_inside(s):
    # Danish letters included: æøåÆØÅ
    # (?i) = case-insensitive
    pattern = r"(?i)^([A-Za-zÆØÅæøå]+).*?\1$"
    match = re.match(pattern, s)
    if match:
        return match.group(1)   # original casing
    return s