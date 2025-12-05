from fastapi import APIRouter, File, UploadFile, HTTPException
from utils.pdf_loader import extract_text_from_pdf
from services.gemini_extract import extract_contract_info

router = APIRouter()

@router.post("/analyze", response_model=dict)
async def analyze_pdf(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf"]:
        raise HTTPException(400, detail="Le fichier doit être un PDF")

    # Taille max PDF
    size_mb = file.size / (1024 * 1024)
    if size_mb > 15:
        raise HTTPException(413, detail="PDF trop volumineux (limite : 15 MB)")

    # Extraction texte
    text = await extract_text_from_pdf(file.file)

    # LLM
    result = await extract_contract_info(text)

    return {"analysis_result": result}
