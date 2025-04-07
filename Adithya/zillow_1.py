import requests
from time import sleep

def zillow_api_call(url):
    url = "https://api.brightdata.com/datasets/v3/trigger"
    headers = {
        "Authorization": "Bearer 473faa2c001050005a9db075d911ff2fa99ab78c56518a70477028e59a342490",
        "Content-Type": "application/json",
    }
    params = {
        "dataset_id": "gd_lfqkr8wm13ixtbd8f5",
        "include_errors": "true",
    }
    data = [
        {"url":url},
    ]
    response = requests.post(url, headers=headers, params=params, json=data)
    return(response.json()['snapshot_id'])


def snapshot_id_parse(snapshotID):
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshotID}"
    snapshot_headers = {"Authorization": "Bearer 473faa2c001050005a9db075d911ff2fa99ab78c56518a70477028e59a342490"}
    data = requests.request('GET', snapshot_url, headers=snapshot_headers).text
    print(type(data))
    return
    # retry_count = 0
    # while (data['status'] == 'running' and retry_count<3):
    #     retry_count+=1
    #     print(f"Retrying {retry_count}, will sleep for 30 seconds")
    #     sleep(30)
    #     data = requests.request('GET', snapshot_url, headers=snapshot_headers).text
    # print(data)
    
snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/?t=for_sale"))