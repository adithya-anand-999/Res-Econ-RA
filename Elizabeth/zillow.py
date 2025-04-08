import requests

# url = "https://api.brightdata.com/datasets/v3/trigger"
# headers = {
# 	"Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad",
# 	"Content-Type": "application/json",
# }
# params = {
# 	"dataset_id": "gd_lfqkr8wm13ixtbd8f5",
# 	"include_errors": "true",
# 	"type": "discover_new",
# 	"discover_by": "input_filters",
# }
# data = [
# 	{"location":"New York","listingCategory":"House for rent","HomeType":"Houses","days_on_zillow":"1 day"},
# 	{"location":"02118","listingCategory":"House for sale","HomeType":"Condos","days_on_zillow":""},
# 	{"location":"Colorado","listingCategory":"","HomeType":"","days_on_zillow":""},
# ]

# response = requests.post(url, headers=headers, params=params, json=data)
# print(response.json())

# url = "https://api.brightdata.com/datasets/v3/snapshot/s_m97ramft1v86mhd850"

# headers = {"Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad"}

# response = requests.request("GET", url, headers=headers)

# print(response.text)

from googlesearch import search

# def get_realtor_url(address):
#     query = f'site:realtor.com "{address}"'
#     for url in search(query, num_results=5):
#         if "realestateandhomes-detail" in url:
#             return url
#     return None

# addresses = [
#     "478 Station Rd, Amherst MA 01002"
# ]

# for address in addresses:
#     url = get_realtor_url(address)
#     print(f"{address} → {url}")

def get_zillow_url(address):
    query = f'site:zillow.com "{address}"'
    for url in search(query, num_results=5):
        if "zillow.com/homedetails" in url:
            return url.split('?')[0]  # clean up tracking params
    return None

addresses = [
    "478 Station Rd, Amherst MA 01002"
]

for address in addresses:
    url = get_zillow_url(address)
    print(f"{address} → {url}")