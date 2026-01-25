from pydantic import BaseModel, Field
import pandas as pd
from typing import Literal
from taxipred.utils.constants import FEATURE_COLUMNS



class TaxiPredict(BaseModel):
    Trip_Distance_km: float = Field(gt=0, lt=150)
    Trip_Duration_Minutes: float = Field(gt=0, lt=200)
    Day_of_Week: Literal["Weekday", "Weekend"]
    Traffic_Conditions: Literal["Low", "Medium", "High"]
    Weather: Literal["Clear", "Rain", "Snow"]


def encode_trip_features(trip):
    features = {feature: 0 for feature in FEATURE_COLUMNS}
    
    features["Trip_Distance_km"] = trip.Trip_Distance_km
    features["Trip_Duration_Minutes"] = trip.Trip_Duration_Minutes
    
    features["Day_of_Week_Weekend"] = 1 if trip.Day_of_Week == "Weekend" else 0

    features["Traffic_Conditions_Low"] = 1 if trip.Traffic_Conditions == "Low" else 0
    features["Traffic_Conditions_Medium"] = 1 if trip.Traffic_Conditions == "Medium" else 0
# High traffic if low and medium == 0

    features["Weather_Rain"] = 1 if trip.Weather == "Rain" else 0
    features["Weather_Snow"] = 1 if trip.Weather == "Snow" else 0
# Clear waether if snow and rain == 0
   
    return pd.DataFrame([features], columns=FEATURE_COLUMNS)




    
