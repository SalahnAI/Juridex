import pdfplumber
import pytesseract
from app.core.logger import logger

async def extract_text_from_pdf(file_obj):
    text = ""

    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                logger.info("Page scannée détectée → OCR")
                img = page.to_image(resolution=300).original
                text += pytesseract.image_to_string(img)

    return text
