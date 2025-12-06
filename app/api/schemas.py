from pydantic import BaseModel, field_validator
from typing import List

class ContractExtraction(BaseModel):
    type_contrat: str
    date_debut: str
    date_fin: str
    parties: List[str]
    montants: List[str]
    obligations: List[str]
    clauses_risque: List[str]
    resume: str

    # Auto-cleaning
    @field_validator("*", pre=True)
    def clean_strings(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v
