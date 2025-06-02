# required libraries for function get_capacity_factor
import urllib.request
import json
from config import PV_API_KEY

# required libraries for testing function, uncomment if running testing block at end. 
# import openpyxl

"""
The function get_capacity_factor() takes in latitude and longitude coordinates 
and the PVWatts api key, defaulted to the key designated in the config.py file. 
The parameters are used to query the PVWatts API and return the DC Capacity Factor data.   
"""

def get_capacity_factor(lat, lon, api_key = PV_API_KEY): # lat = latitude and lon = longitude coordinates, extracted from street address using get_coordinates()
    pv_url = f"https://developer.nrel.gov/api/pvwatts/v8.json?api_key={api_key}&lat={lat}&lon={lon}&system_capacity=4&module_type=0&losses=14.08&tilt=20&azimuth=180&array_type=0" 
    # the above line constructs a url used to call the PVWatts API, the url takes in your PV_API_KEY and the latitude and longitude parameters 
    # currently, the additional request parameters in the url are set to their defaults, please see the PVWatts API documentation to include advanced parameters or modify the defaults 
    response = urllib.request.urlopen(pv_url) # sends a request using the url and stores the json result in "response"
    pv_data = json.loads(response.read()) # the response json is read and loaded into a dictionary stored in "pv_data"
    return pv_data["outputs"]["capacity_factor"] # the capacity factor value is read and returned from "pv_data"

# code to test our function, make sure to uncomment above library imports to run
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active
# test_addr = ws.cell(row=8, column=1).value
# lat = ws.cell(row=8, column=2).value
# lon = ws.cell(row=8, column=3).value
# print(get_capacity_factor(lat, lon))


