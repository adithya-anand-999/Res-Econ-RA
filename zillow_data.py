# required libraries for function get_snapshot_id and get_zillow_data
import requests
from time import sleep

# required libraries for testing function, uncomment if running testing block at end. 
# import openpyxl

from config import BRIGHT_DATA # API key for Bright Data APIs

# NOTE How to add other data point for zillow collection 
# We found our keys by reading the raw JSON output from our API call, comparing the values we wanted with their respective key in the JSON data. Through this we found the elements of 'required_keys'
# which are the keys whose values are the data points we were asked to collect. If one wanted to find additional data points the workflow would be as follows. Choose some sample address and run the 
# below 2 functions but modify get_zillow_data to print out 'data' which contains the entire JSON output of our API call. Now for each additional data point to collect see which key contains that value 
# in 'data'. To note, sometimes the values could be nested within multiple keys, an example of this for us was heating and cooling; if this occurs one would have to navigate through the JSON tree, 
# one can use how we found heating and cooling as an example of how to accomplish this. 

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

    # the heating and cooling keys are further nested in the dataset, within a section called "interior_full"
    payload["heating"] = payload["cooling"] = None # initializes "heating" and "cooling" fields in "payload" to none
    if data["interior_full"] != None: # checks that the "interior_full" section exists
        for dict in data['interior_full']: # loops through each dictionary in "interior_full"
            if dict['title'] == "Heating": payload['heating'] = dict['values'][0].split(": ")[1] # if the "Heating" key is found the value is cleaned (to get the value alone) and stored in "payload"
            if dict['title'] == "Cooling": payload['cooling'] = dict['values'][0].split(": ")[1] # if the "Cooling" key is found the value is cleaned (to get the value alone) and stored in "payload"
    return payload # returns "payload" with updated data 


# code to test our function, make sure to uncomment above library imports to run
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active
# test_url = ws.cell(row=4, column=6).value
# test_data = get_zillow_data(get_snapshot_id(test_url))
# print(test_data)
