from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
import pandas as pd 
from sqlalchemy.orm import Session

from api.latency import LatencyTimer
from api.model_loader import load_model_with_metadata
from api.schemas import EmployeeFeatures

from api.db.base import Base
from api.db.session import SessionLocal, engine
from api.db.deps import get_db
from api.db.models import PredictionLog

app = FastAPI(title = "Employee Attrition Prediction API")

# Create tables at startup
Base.metadata.create_all(bind=engine)
# Load mode and metadata once at startup
model, modelMetadata = load_model_with_metadata()

@app.get("/")
def home():
    return JSONResponse(
        status_code=200,
        content = {"message": "Welcome to the Employee Attrition Prediction Backend API!"}
    )

@app.get("/health")
def health():
    return{
        "status": "ok",
        "model": {
            "name": modelMetadata["model_name"],
            "version": modelMetadata["model_version"],
            "alias": modelMetadata["model_alias"],
            "run_id": modelMetadata["model_run_id"]
        }
    }

@app.post("/predict")
def predict(
    features :EmployeeFeatures,
    db: Session = Depends(get_db)
):
    timer = LatencyTimer()
    timer.start()
    # Convert input into DataFrame
    inputDF = pd.DataFrame([features.model_dump()])
    prediction = model.predict(inputDF)[0]
    probability = model.predict_proba(inputDF)[0][1]

    latency_ms = timer.stop()

    # Log prediction to database
    log = PredictionLog(
        input_data = features.model_dump(),
        prediction = int(prediction),
        probability = float(probability),
        latency_ms = latency_ms,
        model_name = modelMetadata["model_name"],
        model_alias = modelMetadata["model_alias"],
    )

    db.add(log)
    db.commit()

    return{
        "attrition_prediction": int(prediction),
        "attrition_probability": round(float(probability), 4),
        "latency_ms" : latency_ms
    }