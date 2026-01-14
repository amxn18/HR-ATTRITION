import os

os.environ["MLFLOW_TRACKING_URI"] = "sqlite:///mlflow.db"

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

MODEL_NAME = "hr_attrition_model"
MODEL_ALIAS = "Production"


def load_model_with_metadata():
    """
    Loads the ML model from MLflow Registry using alias
    and fetches model version metadata.
    """
    client = MlflowClient()

    model_version = client.get_model_version_by_alias(
        name=MODEL_NAME,
        alias=MODEL_ALIAS
    )

    model_uri = f"models:/{MODEL_NAME}@{MODEL_ALIAS}"
    model = mlflow.sklearn.load_model(model_uri)

    metadata = {
        "model_name": MODEL_NAME,
        "model_version": model_version.version,
        "model_alias": MODEL_ALIAS,
        "run_id": model_version.run_id
    }

    return model, metadata
