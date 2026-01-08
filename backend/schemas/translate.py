from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "សួស្តី"
            }
        }

class TranslateResponse(BaseModel):
    original_text: str
    cleaned_text: str
    royal_text: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "original_text": "សួស្តី",
                "cleaned_text": "សួស្តី",
                "royal_text": "សួស្តី"
            }
        }