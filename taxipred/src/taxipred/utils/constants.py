from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data"
CLEANED_DATA_PATH = BASE_DIR / "data" / "cleaned_data.csv"

JOBLIB_PATH = BASE_DIR / "models"
MODEL_PATH = JOBLIB_PATH / "taxi_price_model.joblib"
SCALER_PATH = JOBLIB_PATH / "taxi_price_scaler.joblib"

FEATURE_COLUMNS = [
    "Trip_Distance_km",
    "Trip_Duration_Minutes",
    "Day_of_Week_Weekend",
    "Traffic_Conditions_Low",
    "Traffic_Conditions_Medium",
    "Weather_Rain",
    "Weather_Snow",
]