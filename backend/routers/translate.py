from fastapi import APIRouter, HTTPException
from schemas.translate import TranslateRequest, TranslateResponse
from utils.preprocessing import clean_text
from ml.inference import get_model

router = APIRouter()

@router.post("/", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    """
    Convert normal Khmer text to Royal Khmer text.
    
    Flow: User Input -> Preprocessing -> Inference -> Output
    """
    try:
        # Step 1: Get user input
        original_text = req.text
        
        if not original_text or not original_text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        # Step 2: Preprocessing - clean the text
        cleaned_text = clean_text(original_text)
        
        if not cleaned_text:
            raise HTTPException(
                status_code=400, 
                detail="Text contains no valid Khmer characters after preprocessing"
            )
        
        # Step 3: Inference - convert to Royal Khmer
        model = get_model()
        royal_text = model.predict(original_text)  # predict uses clean_text internally
        
        # Step 4: Return output
        return TranslateResponse(
            original_text=original_text,
            cleaned_text=cleaned_text,
            royal_text=royal_text
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Translation error: {str(e)}"
        )
