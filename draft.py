import requests

endpoint_sheety_post = "https://api.sheety.co/20224e35b353a9c610f586f6e7ab56ce/workoutTracking/workouts"

# headers = {
#     "Authorization": "Bearer SecretTokenWorkouuut)"
# }

payload = {
    "workout":{
        "date": "16/10/21",
        "time": "15:00:00"  ,
        "exercise": "fucking so hard with that fucking Sheety servisce",
        "duration": "one million years",
        "calories": "infinity"
    }
}

response = requests.post(url=endpoint_sheety_post, json=payload)
print(response.text)
NUTRITION_IX_ID = "21dea064"
NUTRITION_IX_KEY="ddd358774b300402c56a2aa076d9dc3f"
SHEETY_TOKEN="SecretTokenWorkouuut)"