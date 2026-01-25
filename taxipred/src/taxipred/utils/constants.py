from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data"

CLEANED_DATA_PATH = Path(__file__).parent.parent / "data" / "cleaned_data.csv"

JOBLIB_PATH = Path(__file__).parent.parent / "models"

MODEL_PATH = JOBLIB_PATH / "taxi_price_model.joblib"
SCALER_PATH = JOBLIB_PATH / "taxi_price_scaler.joblib"

SCALER_PATH = Path

FEATURE_COLUMNS = [
    "Trip_Distance_km",
    "Trip_Duration_Minutes",
    "Day_of_Week_Weekend",
    "Traffic_Conditions_Low",
    "Traffic_Conditions_Medium",
    "Weather_Rain",
    "Weather_Snow",
]