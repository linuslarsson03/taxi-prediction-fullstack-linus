from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from pydantic import BaseModel

from taxipred.utils.constants import DATA_PATH, MODEL_PATH, SCALER_PATH
from taxipred.backend.data_processing import TaxiPredict, encode_trip_features

app = FastAPI()

router = APIRouter(prefix="/api/taxi")

df = pd.read_csv(DATA_PATH / "taxi_trip_pricing.csv")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


class PredictTaxiPrice(BaseModel):
    predicted_price: float


@router.get("")
def read_data():
     return df.to_dict(orient="records")


@router.post("/predict", response_model=PredictTaxiPrice)
def predict_price(trip_data: TaxiPredict):
    X = encode_trip_features(trip_data)
    scaled_X = scaler.transform(X)
    prediction = model.predict(scaled_X)[0]

    return {"predicted_price": float(prediction)}




app.include_router(router=router)