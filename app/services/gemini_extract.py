import google.generativeai as genai
from app.core.config import settings
from app.services.prompts import build_extraction_prompt
from app.utils.json_fixer import fix_json
from app.api.schemas import ContractExtraction
from app.services.chunking import chunk_text

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(settings.MODEL_NAME)


async def extract_contract(text: str):
    chunks = chunk_text(text)
    merged = {
        "type_contrat": "",
        "date_debut": "",
        "date_fin": "",
        "parties": [],
        "montants": [],
        "obligations": [],
        "clauses_risque": [],
        "resume": ""
    }

    for c in chunks:
        prompt = build_extraction_prompt(c)
        response = model.generate_content(prompt, generation_config={"temperature": 0})

        try:
            clean = fix_json(response.text)
            validated = ContractExtraction(**clean)
        except Exception:
            # fallback #2 : re-demander au LLM de corriger
            fix_prompt = f"""
Corrige ce JSON et renvoie un JSON strict :

{response.text}
"""
            res2 = model.generate_content(fix_prompt, generation_config={"temperature": 0})
            clean = fix_json(res2.text)
            validated = ContractExtraction(**clean)

        # merge des valeurs
        merged["parties"] += validated.parties
        merged["montants"] += validated.montants
        merged["obligations"] += validated.obligations
        merged["clauses_risque"] += validated.clauses_risque
        
        # champs simples : on garde le premier trouvé
        for k in ["type_contrat", "date_debut", "date_fin", "resume"]:
            if merged[k] == "" and getattr(validated, k) != "":
                merged[k] = getattr(validated, k)

    return ContractExtraction(**merged)
