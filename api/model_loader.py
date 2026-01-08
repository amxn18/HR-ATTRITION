import mlflow
import mlflow.sklearn

MODEL_URI = ""

def loadModel():
    """
    Loads the production model from Mlflow Registory.
    This should be called once at application startup
    """

    model = mlflow.sklearn.load_model(MODEL_URI)
    return model