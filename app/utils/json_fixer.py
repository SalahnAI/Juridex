import re, json

def extract_json(raw):
    match = re.search(r"\{[\s\S]*\}", raw)
    if not match:
        raise ValueError("Aucun JSON trouvé")
    return match.group(0)

def fix_json(raw):
    json_str = extract_json(raw)

    # Fix syntaxique automatique
    fixes = [
        (r",\s*}", "}"),
        (r",\s*]", "]"),
        (r"[\n\r]", " "),
        (r"\s+", " "),
    ]
    for pattern, repl in fixes:
        json_str = re.sub(pattern, repl, json_str)

    return json.loads(json_str)
