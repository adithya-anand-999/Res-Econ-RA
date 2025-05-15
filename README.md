# Residential Solar PV Data Collection 
API and web scraping data collection conducted with the Resources Economics Department at the University of Massachusetts — Amherst. 

## Overview
The attached code gathers data across three different websites, NREL's PVWatts Calculator, Google's Project Sunroof, and Zillow.  Below please find the setup and methodology implemented for each website: 

### Setup: Longitude and Latitude



### Wesbite One: NREL's PVWatts Calculator
The function get_cap_factor takes in latitude and longitude coordinates and uses those coordinates to query the PVWatts API and return the  DC Capacity Factor data.  The loop iterates through the addresses coordinates in the address_cord json file, calls get_cap_factor on each set of coordinates, the results, alongside the original address, latitude, longitude, on which the function was called, are stored in a dictionary and appended to a list.  The code commented out writes the information from the list to an excel document such that each field in the dictionary is a column. 


## Usage Instructions

## Sources 

## Contact 
