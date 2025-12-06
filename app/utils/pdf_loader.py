import google.generativeai as genai
import pypdfium2 as pdfium
from io import BytesIO
from PIL import Image
from app.core.config import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(settings.MODEL_NAME)

async def extract_text_from_pdf(file):
    pdf = pdfium.PdfDocument(file)
    full_text = ""

    for page_index in range(len(pdf)):
        page = pdf.get_page(page_index)
        pil_image = page.render(scale=2).to_pil()

        # Convert PIL → bytes
        img_buffer = BytesIO()
        pil_image.save(img_buffer, format="PNG")
        img_buffer.seek(0)

        # Gemini Vision OCR
        result = model.generate_content([
            "Extract text from this document page. Return ONLY the text.",
            {"mime_type": "image/png", "data": img_buffer.getvalue()}
        ])

        full_text += result.text + "\n"

    return full_text
