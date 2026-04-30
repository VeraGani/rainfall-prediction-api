# 🌧️ Rain Predictor - Streamlit App

Live API
https://rainfall-prediction-api-omns.onrender.com/docs

## Overview
This project is a rainfall prediction system originally developed as part of an academic machine learning assignment and later extended into a cloud-deployed backend API.

The system includes:

A FastAPI backend for prediction services
A Streamlit web app for user interaction
A machine learning model built using AutoML (TPOT)

## Features

# Cloud API (Primary)
REST API built with FastAPI
Endpoints:
/predict — rainfall prediction
/health — system status
Deployed to cloud using Render
Public API accessible via URL

## Machine Learning
Model built using TPOT AutoML
Trained on Australian weather dataset
Optimized for high recall (minimize missed rain events)

## Technologies
- Python
- FastAPI (backend API)
- Streamlit (frontend UI)
- Render (cloud deployment)
- Pandas / Scikit-learn (ML pipeline)

## Example API Request

```json
{
  "rain_mm": 2,
  "humidity_3pm": 80,
  "pressure_3pm": 1005,
  "wind_speed_3pm": 25,
  "temp_3pm": 22
}
```

## Project Structure

```
## 📁 Project Structure

```
rainfall-prediction-api/
├── main.py                    # FastAPI backend (cloud-deployed API)
├── app.py                     # Streamlit web application
├── requirements.txt           # Dependencies
├── README.md
├── images/                    # Screenshots for documentation
├── rain_predictor_model.pkl   # Trained ML model (used in original version)
├── preprocessing_info.pkl     # Feature preprocessing metadata
├── rainfall_clean.csv         # Processed dataset
├── Australia Rainfall.csv     # Original dataset
├── EmergingAI_assignment_3.ipynb  # Notebook (model development)
```
```
