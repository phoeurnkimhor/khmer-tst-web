from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.config import FRONTEND_URLS
from configs.config import checkpoint_path
from routers import translate
from ml.inference import initialize_model
import os

app = FastAPI(
    title="Khmer Text to Royal Khmer Converter",
    description="API for converting normal Khmer text to Royal Khmer text",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_URLS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """
    Initialize the ML model on application startup.
    """
    try:
        initialize_model(checkpoint_path)
        print(f"✓ Model loaded successfully from {checkpoint_path}")
    except Exception as e:
        print(f"✗ Failed to load model: {str(e)}")
        print("API will start but translation endpoint will fail until model is loaded.")

@app.get("/")
async def root():
    return {
        "message": "Khmer to Royal Khmer Text Converter API",
        "endpoints": {
            "translate": "/translate/",
            "docs": "/docs",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    from ml.inference import model
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

app.include_router(
    translate.router,
    prefix="/translate",
    tags=["Translate"]
)
