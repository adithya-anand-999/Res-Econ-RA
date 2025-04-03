import urllib.request
import json
import pandas as pd

"""
The function get_cap_factor takes in latitude and longitude coordinates 
and uses those coordinates to query the PVWatts API and return the 
DC Capacity Factor data.  The loop iterates through the addresses 
coordinates in the address_cord json file, calls get_cap_factor on 
each set of coordinates, the results, alongside the original address, 
latitude, longitude, on which the function was called, are stored in a
dictionary and appended to a list.  The code commented out writes the 
information from the list to an excel document such that each field 
in the dictionary is a column. 
"""

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel("Address.xls")
address_cord_file = "address_cord.json"
with open(address_cord_file, "r") as file:
  address_cord = json.load(file)   

pv_api_key = "sVziuCWgyCFMyXRchyZ60wAWcHQACb5f1x0TOQ74"
def get_cap_factor(lat, lon): 
    pv_url = f"https://developer.nrel.gov/api/pvwatts/v8.json?api_key={pv_api_key}&lat={lat}&lon={lon}&system_capacity=4&module_type=0&losses=14.08&tilt=20&azimuth=180&array_type=0" 
    response = urllib.request.urlopen(pv_url)
    pv_data = json.loads(response.read())
    return pv_data["outputs"]["capacity_factor"]

with_cap_factor = []
for address, (lat, lon) in address_cord.items(): 
   capacity_factor = get_cap_factor(lat, lon)
   with_cap_factor.append({
      "Address": address,
      "Latitude": lat,
      "Longitude": lon,
      "Capacity Factor": capacity_factor
   })

# print(with_cap_factor) 
# new_df = pd.DataFrame(with_cap_factor)
# new_df.to_excel("with_capacity_factor_2.xlsx", index=False, engine="openpyxl")



