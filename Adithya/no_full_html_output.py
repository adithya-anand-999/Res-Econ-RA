import requests
required_keys = ["zestimate", "taxAssessedValue", "dateSoldString", "livingArea", "yearBuilt", "lotAreaValue", "lotAreaUnits"]

# url = "https://api.brightdata.com/datasets/v3/trigger"
# headers = {
# 	"Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad",
# 	"Content-Type": "application/json",
# }
# params = {
# 	"dataset_id": "gd_lfqkr8wm13ixtbd8f5",
# 	"include_errors": "true",
# }
# data = [
# 	{"url":"https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/?t=for_sale"},
# ]

# response = requests.post(url, headers=headers, params=params, json=data)
# print(response.json())

# url = "https://api.brightdata.com/datasets/v3/snapshot/s_m993ow1q27wmb1cluh"

# headers = {"Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad"}

# api_response = requests.request("GET", url, headers=headers)

response = api_response

payload = {}
# for key in required_keys:
#     payload[key] = response.get(key, None)
#     interior_data = response['interior']
# payload["heating"] = interior_data.get('heating', None)
# payload['cooling'] = interior_data.get('cooling', None)

# print(response.text)
print(payload)