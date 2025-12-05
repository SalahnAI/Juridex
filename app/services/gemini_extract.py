import google.generativeai as genai
from core.config import settings
from core.logger import logger

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
