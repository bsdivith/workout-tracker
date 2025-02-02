from http.client import responses
from datetime import datetime
import requests
import os

APP_ID =os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
nutritionx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

date = datetime.today()

GENDER = "male"
AGE = "22"
WEIGHT ="55"
HEIGHT = "168"


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
data = {
    "query": input("Enter exercise or activity: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(url=nutritionx_endpoint,json=data,headers=header)
duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']
exercise = response.json()['exercises'][0]['name']
row_data = {
    "workout":{
    "date": date.strftime("%d/%m/%Y"),
    "time": date.strftime("%H:%M:%S"),
    "exercise": exercise.title(),
    "duration": duration,
    "calories": calories,
}}
BEARER =os.environ.get("BEARER_TOKEN")
bearer_headers = {"Authorization": f"Bearer {BEARER}"}
sheety_response = requests.post(url=sheety_endpoint, json=row_data, headers=bearer_headers)
print(sheety_response.text)
