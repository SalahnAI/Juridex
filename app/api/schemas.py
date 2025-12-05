from pydantic import BaseModel

class PDFAnalysisResponse(BaseModel):
    analysis_result: str
