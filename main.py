from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Rainfall Prediction API")


class WeatherInput(BaseModel):
    rain_mm: float
    humidity_3pm: float
    pressure_3pm: float
    wind_speed_3pm: float
    temp_3pm: float


@app.get("/")
def home():
    return {"message": "Rainfall Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: WeatherInput):
    risk_score = 0

    if data.rain_mm > 0:
        risk_score += 1
    if data.humidity_3pm > 70:
        risk_score += 1
    if data.pressure_3pm < 1010:
        risk_score += 1
    if data.wind_speed_3pm > 20:
        risk_score += 1

    probability = min(risk_score / 4, 1.0)
    prediction = "Rain" if probability >= 0.5 else "No Rain"

    if probability < 0.3:
        risk_level = "LOW"
        recommendation = "Low risk of rain. Outdoor events are likely safe."
    elif probability < 0.6:
        risk_level = "MODERATE"
        recommendation = "Moderate risk of rain. Have a backup plan ready."
    else:
        risk_level = "HIGH"
        recommendation = "High risk of rain. Consider moving indoors."

    return {
        "prediction": prediction,
        "rain_probability": probability,
        "risk_level": risk_level,
        "recommendation": recommendation
    }