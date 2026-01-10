import mlflow
import mlflow.sklearn

MODEL_NAME = "hr_attrition_model"
MODEL_ALIAS = "Production"

def loadModel():
    """
    Loads the production model from Mlflow Registory.
    This should be called once at application startup
    """

    model = mlflow.sklearn.load_model(model_uri)

    metadata = {
        "model_name": MODEL_NAME,
        "model_version": model_version.version,
        "model_alias": MODEL_ALIAS,
        "run_id": model_version.run_id
    }

    return model, metadata
