import requests
import json
import datetime
import os

NUTRITION_IX_ID = "21dea064"
NUTRITION_IX_KEY="ddd358774b300402c56a2aa076d9dc3f"
SHEETY_TOKEN="SecretTokenWorkouuut)"

endpoint_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint_sheety_post = "https://api.sheety.co/20224e35b353a9c610f586f6e7ab56ce/workoutTracking/workouts"
user_says = str(input("What have you done today? :"))

headers_nutritionix = {
    "x-app-id": NUTRITION_IX_ID,
    "x-app-key": NUTRITION_IX_KEY
}
headers_sheety = {
    "Authorization": "Bearer SecretTokenWorkouuut)"
}
parameters = {
    "query": user_says,
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 185,
    "age": 22
}


response = requests.post(url=endpoint_nutritionix, json=parameters, headers=headers_nutritionix)
print(f"this is .text: {response.text}")
raw_data_json = json.loads(response.text)
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
print(date)
print(time)

for exercise_data in raw_data_json["exercises"]:
    exercise_name = exercise_data["name"].title()
    exercise_duration = int(exercise_data["duration_min"])
    exercise_calories = float(exercise_data["nf_calories"])
    parameters_sheety = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }
    response_sheety = requests.post(url=endpoint_sheety_post,
                                    json=parameters_sheety,
                                    headers=headers_sheety)
    print(response_sheety.text)