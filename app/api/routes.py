from fastapi import APIRouter, File, UploadFile, HTTPException
from app.utils.pdf_loader import extract_text_from_pdf
from app.services.gemini_extract import extract_contract
from app.api.schemas import ContractExtraction

router = APIRouter()


@router.post("/analyze", response_model=ContractExtraction)
async def analyze_pdf(file: UploadFile = File(...)):
    # Vérification type
    if file.content_type != "application/pdf":
        raise HTTPException(400, detail="Le fichier doit être un PDF.")

    # Taille maximale
    size_mb = file.size / (1024 * 1024) if hasattr(file, "size") else 0
    if size_mb > 20:
        raise HTTPException(413, detail="Fichier trop volumineux (limite : 20 MB).")

    # 1️⃣ OCR + extraction texte
    text = await extract_text_from_pdf(file.file)

    if len(text.strip()) == 0:
        raise HTTPException(422, detail="Impossible d'extraire le texte du PDF.")

    # 2️⃣ Traitement du LLM robuste (chunking + validation + réparation)
    result = await extract_contract(text)

    # 3️⃣ Retour JSON strict validé par Pydantic
    return result
