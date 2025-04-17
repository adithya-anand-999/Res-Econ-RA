import requests
from time import sleep
import json
import pandas as pd
import openpyxl

required_keys = ["zestimate", "taxAssessedValue", "dateSoldString", "livingArea", "yearBuilt", "lotAreaValue", "lotAreaUnits"]
# website_3_data_path = r"./Adithya/website_3_data.json"
# with open(website_3_data_path, "r") as file:
#     content = file.read().strip()
#     website_3_data = None if not content else json.load(file)
# print(website_3_data)

def zillow_api_call(addr):
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": "Bearer 13045b9674ca543e98b3768901c6799a2b876aff0220e26d61c9dae63dfeec0a",
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
    snapshot_headers = {"Authorization": "Bearer 13045b9674ca543e98b3768901c6799a2b876aff0220e26d61c9dae63dfeec0a"}
    snapshot_data = requests.request('GET', snapshot_url, headers=snapshot_headers).json()
    retry_count = 0

    while 'status' in snapshot_data and retry_count < 3:
        retry_count += 1
        print(f"Retrying {retry_count}, sleeping 30s…")
        sleep(30)
        snapshot_data = requests.get(snapshot_url, headers=snapshot_headers).json()

    if 'status' in snapshot_data:
        print(f"Scraping failed for snapshot {snapshotID}")
        return None
    
    # print(snapshot_data)
    # readable_output = snapshot_data
    payload = {}
    for key in required_keys:
        payload[key] = snapshot_data.get(key, None)
    print(payload)
    payload["heating"], payload["cooling"] = None, None
    if "interior_full" in snapshot_data:
        print(1)
        for dict in snapshot_data['interior_full']:
            if dict['title'] == "Heating": payload['heating'] = dict['values'][0].split(": ")[1]
            if dict['title'] == "Cooling": payload['cooling'] = dict['values'][0].split(": ")[1]
    return payload

# code to test functions    
# snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/150-Traincroft-NW-Medford-MA-02155/56277119_zpid/"))
# print(snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/")))
# print(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/"))

wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
ws = wb.active

for row in range(11,13):
    url = ws.cell(row=row, column=6).value
    print(url)
    data = snapshot_id_parse(zillow_api_call(url))
    # print(data)
    if data == None: continue
    for i,point in enumerate(data.values()):
        ws.cell(row=row, column=7+i, value=point if point else "None")
    wb.save('res-econ_RA_data.xlsx')
    print(f"data collection for {url} done")
    sleep(5)


# df = pd.read_excel('res-econ_RA_data.xlsx', engine='openpyxl')
# column_6 = list(df.iloc[:, 5])[11:36]

# for addr in column_6[:3]:
#     website_3_data[addr] = snapshot_id_parse(zillow_api_call(addr))

# with open(website_3_data_path, "w") as f:
#     json.dump(website_3_data, f, indent=4)

# print("done writing and scraping")