import requests

NUTRITION_IX_ID = "21dea064"
NUTRITION_IX_KEY = "ddd358774b300402c56a2aa076d9dc3f"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_says = str(input("What have you done today? :"))

headers = {
    "x-app-id": NUTRITION_IX_ID,
    "x-app-key": NUTRITION_IX_KEY
}

parameters = {
    "query": user_says,
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 185,
    "age": 22
}

response = requests.post(url=endpoint, json=parameters, headers=headers)
print(response)
print(response.text)