from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

from api.model_loader import load_model_with_metadata
from api.schemas import EmployeeFeatures
from api.latency import LatencyTimer

app = FastAPI(title="HR Attrition Prediction API")

# Load model + metadata ONCE at startup
model, model_metadata = load_model_with_metadata()


@app.get("/")
def home():
    return JSONResponse(
        status_code=200,
        content={"message": "Welcome to HR-Attrition backend API"}
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": {
            "name": model_metadata["model_name"],
            "version": model_metadata["model_version"],
            "alias": model_metadata["model_alias"],
            "run_id": model_metadata["run_id"]
        }
    }


@app.post("/predict")
def predict(features: EmployeeFeatures):
    timer = LatencyTimer()
    timer.start()

    input_df = pd.DataFrame([features.model_dump()])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    latency_ms = timer.stop()

    return {
        "attrition_prediction": int(prediction),
        "attrition_probability": round(float(probability), 4),
        "latency_ms" : latency_ms
    }
