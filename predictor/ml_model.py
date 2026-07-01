import os
import joblib

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "ml",
    "models",
    "logistic_model.pkl",
)

SCALER_PATH = os.path.join(
    PROJECT_DIR,
    "ml",
    "models",
    "scaler.pkl",
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)