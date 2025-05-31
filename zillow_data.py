# required libraries we use.
import requests
from time import sleep

# libraries for testing
# import openpyxl

from config import BRIGHT_DATA # API key for Bright Data APIs

#TODO: explain how to get other datapoints, other keys 

# data points we are collecting
required_keys = ["zestimate", "taxAssessedValue", "taxAssessedYear", "dateSoldString", "livingArea", "yearBuilt", "lotAreaValue", "lotAreaUnits"]

"""
The function get_snapshot_id() takes in a zillow url, obtained via get_zillow_url(),
and converts that url to a unique Snapshot id.  More information about snapshot ID can be found 
at https://docs.brightdata.com/api-reference/web-scraper-api/trigger-a-collection, 
it is a step in the data collection framework found for Bright Data.
Bright Data provides a third party Zillow API used to collect our data points.
get_snapshot_id() is taken directly from Bright Data's usage guidelines. 

"""

def get_snapshot_id(addr_url, bright_data_key = BRIGHT_DATA): # addr_url = Zillow url
    # boilerplate code from Bright Data website 
    url = "https://api.brightdata.com/datasets/v3/trigger" 
    headers = {
        "Authorization": bright_data_key, # sets up the HTTP request headers using the Bright Data API Key stored in config.py
        "Content-Type": "application/json",
    }
    params = {
        "dataset_id": "gd_lfqkr8wm13ixtbd8f5",
        "include_errors": "true",
    }
    data = [
        {"url":addr_url},
    ]
    response = requests.post(url, headers=headers, params=params, json=data)
    return(response.json()['snapshot_id'])  # snapshot_id is a pointer to a zillow data object for this address


"""
The function get_zillow_data() takes in the snapshot ID produced by get_snapshot_id(). 
The function then parses that snapshot ID producing a json object with all the data 
for the address. From the json object, we find and collect the specific data points required.
"""
def get_zillow_data(snapshotID, bright_data_key = BRIGHT_DATA):
    # boilerplate code from Bright Data
    url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshotID}" # builds the url to access Bright Data's dataset 
    headers = {"Authorization": bright_data_key} # sets up the HTTP request headers using the Bright Data API Key stored in config.py
    data = requests.request('GET', url, headers=headers).json() # sends a GET request to the Bright Data API, parses the json response stored in "data"

    
    retry_count = 0 # a counter to keep track of retries 

    while 'status' in data and retry_count < 3: # retries to collect data if the key 'status' is found in "data", indicating the dataset is not yet available, allows for three retries
        retry_count += 1 
        print(f"Zillow Data Collection: Retrying {retry_count}, sleeping 30s…") 
        sleep(30) # waits thirty seconds before sending another GET request to obtain data, a thirty second wait was recommended by Bright Data
        data = requests.request('GET', url, headers=headers).json() # sends a GET request to the Bright Data API, parses the json response stored in "data"

    if 'status' in data: # if after three retires, the dataset still fails to load, the function prints an error and returns None
        print(f"Scraping failed for snapshot {snapshotID}")
        return None
    
    payload = {} # initializes a dictionary to which each of the required_keys is added with the values found from "data" or None if not found
    for key in required_keys:
        payload[key] = data.get(key, None)
    
    # print(payload)    
    # print(data['interior_full'])
    
    # the heating and cooling keys are further nested in the dataset, within a section called "interior_full"
    payload["heating"] = payload["cooling"] = None # initializes "heating" and "cooling" fields in "payload" to none
    if data["interior_full"] != None: # checks that the "interior_full" section exists
        for dict in data['interior_full']: # loops through each dictionary in "interior_full"
            if dict['title'] == "Heating": payload['heating'] = dict['values'][0].split(": ")[1] # if the "Heating" key is found the value is cleaned (to get the value alone) and stored in "payload"
            if dict['title'] == "Cooling": payload['cooling'] = dict['values'][0].split(": ")[1] # if the "Cooling" key is found the value is cleaned (to get the value alone) and stored in "payload"
    return payload # returns "payload" with updated data 


# open our excel doc
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active

# Code to test our functions
# snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/150-Traincroft-NW-Medford-MA-02155/56277119_zpid/"))
# print(snapshot_id_parse(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/")))
# print(zillow_api_call("https://www.zillow.com/homedetails/2506-Gordon-Cir-South-Bend-IN-46635/77050198_zpid/"))

# converts a URL into final zillow data object with the required fields
# test_url = ws.cell(row=4, column=6).value
# test_data = get_zillow_data(get_snapshot_id(test_url))
# print(test_data)




# # loops over the rows in our excel. Bounds are inclusive of first arg, exclusive of second arg. Use the row numbers found in the excel. So to include row 3 you
# # would set your first arg to 3.
# for row in range(155,211):
#     # grab the url for 'row' found in column 6
#     url = ws.cell(row=row, column=6).value

#     # if url does not exist skips to next url
#     if url == "None": continue
#     print(f"Collecting row {row} with url = {url}")

#     # collect the data for the url
#     data = snapshot_id_parse(zillow_api_call(url))

#     # if data collection for the url failed, snapshot_id_parse will return None. Then this conditional will run skipping this row as no data has been collected.
#     if data == None: continue

#     # for each data point, write to a separate column in our excel, if the data point does not exist we write "None"
#     for i,point in enumerate(data.values()):
#         ws.cell(row=row, column=7+i, value=point if point else "None")
    
#     # as changes have been made to the excel in the above code, save the changes
#     wb.save('res-econ_RA_data.xlsx')
    
#     # print(f"data collection for {url} done")
#     sleep(5)

# print("Data collection finished!")