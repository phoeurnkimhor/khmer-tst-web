from dotenv import load_dotenv
import os

load_dotenv()

FRONTEND_URLS = os.getenv(
    "FRONTEND_URL"
).split(",")

DB_URL = os.getenv("DB_URL")

checkpoint_path = os.getenv(
    "MODEL_CHECKPOINT_PATH",
    "ml/best_model.pt"
)