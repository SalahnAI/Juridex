import google.generativeai as genai
from app.core.config import settings
from app.core.logger import logger

genai.configure(api_key=settings.GEMINI_API_KEY)

async def extract_contract_info(text: str):
    prompt = f"""
    Tu es un expert juridique.
    Extrait en JSON STRICT :

    {{
      "type_contrat": "",
      "date_debut": "",
      "date_fin": "",
      "parties": [],
      "montants": [],
      "obligations": [],
      "clauses_risque": [],
      "resume": ""
    }}

    Texte :
    {text}
    """

    model = genai.GenerativeModel(settings.MODEL_NAME)

    logger.info("Appel API Gemini…")
    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0}
    )

    return response.text

import json
import re

def fix_json(response_text: str):
    # Extraire le JSON entre { ... }
    json_match = re.search(r"\{[\s\S]*\}", response_text)
    if not json_match:
        raise ValueError("Aucun JSON trouvé dans la réponse du LLM")

    json_str = json_match.group(0)

    # Tentative de parsing direct
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        pass

    # Réparation simple : enlever trailing commas
    json_str = re.sub(r",\s*}", "}", json_str)
    json_str = re.sub(r",\s*]", "]", json_str)

    # Dernière tentative
    return json.loads(json_str)
