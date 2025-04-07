import requests
from time import sleep
import json

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
    data = json.loads(requests.request('GET', snapshot_url, headers=snapshot_headers).text)
    # print(type(data))
    # print(data)
    # return
    retry_count = 0
    while ('status' in data and data['status'] == 'running' and retry_count<3):
        retry_count+=1
        print(f"Retrying {retry_count}, will sleep for 30 seconds")
        sleep(30)
        data = json.loads(requests.request('GET', snapshot_url, headers=snapshot_headers).text)
    
    print("output type", type(data))
    readable_output = json.dumps(data,indent=4)
    print(readable_output)
    
snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/150-Traincroft-NW-Medford-MA-02155/56277119_zpid/"))

# print(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/?t=for_sale"))
# snapshot_id_parse("s_m96cewo62057wclm3r")
# snapshot_id_parse()