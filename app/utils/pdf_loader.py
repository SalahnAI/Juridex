import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io

async def extract_text_from_pdf(file_data):
    pdf_bytes = file_data.read()

    images = convert_from_bytes(pdf_bytes)

    full_text = ""

    for img in images:
        text = pytesseract.image_to_string(img, lang="eng")
        full_text += text + "\n"

    return full_text
