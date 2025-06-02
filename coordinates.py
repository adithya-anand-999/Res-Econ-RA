# required libraries for function get_coordinates
from config import API_KEY
import googlemaps

# to run the test at the end of the file, please uncomment the below import 
# import openpyxl

"""
The function get_coordinates() takes in a written address and the google API key, 
defaulted to the key designated in the config.py file. The parameters are used to 
query the Google Maps Geocoding API which converts an address to the returned coordinates. 
"""

def get_coordinates(address, api_key=API_KEY): # address = complete physical address, api_key = Google API Key 
    gmaps = googlemaps.Client(key=api_key) # creates a "Client" object through the googlemaps library using the Google API Key, stored in "gmaps", used to handle authentication  
    geocode_result = gmaps.geocode(address) # calls the Google Maps Geocoding API, converts address to coordinates stored in "geocode_result"
    if geocode_result: # checks that geocode_result is not empty 
        location = geocode_result[0]['geometry']['location'] # accesses the first match (coordinates closest to address) and structure within "geocode_result" that contains the coordinates
        return (location['lat'], location['lng']) # latitude and longitude coordinates are read and returned as a tuple
    return (None) # if "geocode_result" is empty, (None) is returned 


# please uncomment the indicated import and four lines below to test our function
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active
# test_addr = ws.cell(row=8, column=1).value
# print(get_coordinates(test_addr))





