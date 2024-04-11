import os
import requests
from datetime import datetime
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
sheety_ID = os.environ["sheety_ID"]
NL_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

print(APP_ID, APP_KEY, sheety_ID, NL_endpoint)
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

param = {
     "query": input("tell me which exercises you did ? "),
}

res = requests.post(url=NL_endpoint, json=param, headers=headers)
result = res.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_endpoint = f"https://api.sheety.co/{sheety_ID}/workoutTracking/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

