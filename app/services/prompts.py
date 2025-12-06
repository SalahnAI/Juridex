def build_extraction_prompt(text):
    return f"""
Tu es un extracteur JSON strict.

RENVOIE UNIQUEMENT du JSON VALIDE.

Schéma obligatoire :

{{
  "type_contrat": "string",
  "date_debut": "string",
  "date_fin": "string",
  "parties": ["string"],
  "montants": ["string"],
  "obligations": ["string"],
  "clauses_risque": ["string"],
  "resume": "string"
}}

RÈGLES:
- AUCUN texte hors JSON
- PAS de ``` 
- PAS d'explications
- PAS de phrases
- Pas de null : utiliser "" ou []
- JSON strict uniquement

Texte à analyser :
{text}
"""
