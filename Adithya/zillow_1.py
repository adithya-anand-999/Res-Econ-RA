import requests
from time import sleep
import json

required_keys = ["zestimate", "taxAssessedValue", "dateSoldString", "livingArea", "yearBuilt", "lotAreaValue", "lotAreaUnits"]
website_3_data_path = r"C:\Users\Adithya Anand\Documents\College\Junior Year\Res-Econ RA\Res-Econ-RA\Adithya\website_3_data.json"
with open(website_3_data_path, "r") as file:
    content = file.read().strip()
    website_3_data = None if not content else json.load(file)
print(website_3_data)

def zillow_api_call(addr):
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad",
        "Content-Type": "application/json",
    }
    params = {
        "dataset_id": "gd_lfqkr8wm13ixtbd8f5",
        "include_errors": "true",
    }
    data = [
        {"url":addr},
    ]
    response = requests.post(url, headers=headers, params=params, json=data)
    return(response.json()['snapshot_id'])


def snapshot_id_parse(snapshotID):
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshotID}"
    snapshot_headers = {"Authorization": "Bearer 1b7a56093c477c8f5515d144f4c071e8bc714258a3fb90c13a5a2e72fc7bb6ad"}
    snapshot_data = requests.request('GET', snapshot_url, headers=snapshot_headers).json()
    # print(type(data))
    # print(data)
    # return
    retry_count = 0
    while ('status' in snapshot_data or retry_count<3):
        retry_count+=1
        if retry_count>3: return("Scrapping for address has failed.")
        print(f"Retrying {retry_count}, will sleep for 30 seconds")
        sleep(30)   
        snapshot_data = requests.request('GET', snapshot_url, headers=snapshot_headers).json()
    # readable_output = json.dumps(snapshot_data,indent=4)
    readable_output = snapshot_data

    # print(readable_output)
    # building payload of the keys that we desire from the overall API output
    payload = {}
    for key in required_keys:
        payload[key] = readable_output.get(key, None)

    heating_val, cooling_val = None, None
    for dict in readable_output['interior_full']:
        if dict['title'] == "Cooling": payload['cooling'] = dict['values'][0].split(": ")[1]
        if dict['title'] == "Heating": payload['heating'] = dict['values'][0].split(": ")[1]
    # payload["heating"] = response1['interior'].get('heating', None)
    # payload['cooling'] = response1['interior_full'].get('cooling', None)

    # print(response.text)
    print(payload)
    
# snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/150-Traincroft-NW-Medford-MA-02155/56277119_zpid/"))

# print(snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/")))
# print(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/"))


print(snapshot_id_parse("s_m993ow1q27wmb1cluh"))

df = pd.read_excel('res-econ_RA_data.xlsx', engine='openpyxl')
column_6 = df.iloc[:, 5]

print(column_6)