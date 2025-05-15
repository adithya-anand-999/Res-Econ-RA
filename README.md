# Residential Solar PV Data Collection 
API and web scraping data collection conducted with the Resources Economics Department at the University of Massachusetts — Amherst. 

## Overview
The attached code gathers data from a list of addresses across three different websites, NREL's PVWatts Calculator, Google's Project Sunroof, and Zillow.  Below please find the setup and methodology implemented for each website:  

### Setup:

#### config.py

#### Coordinates
PVWatts and Project Sunroof both utilize coordinates to access a locations associated data.  Thus, we first developed the function get_coordinates(), which converts the list of addresses to coordinates via the Google Maps API.

### Wesbites:

#### NREL's PVWatts Calculator
NREL offers publicly available API for their calculator used in our function get_capacity_factor().  The function get_capacity_factor() takes in latitude and longitude coordinates from get_coordinates to query the PVWatts API and return the  DC Capacity Factor data.  The loop iterates through the addresses coordinates in the address_cord json file, calls get_cap_factor on each set of coordinates, the results, alongside the original address, latitude, longitude, on which the function was called, are stored in a dictionary and appended to a list.  The code commented out writes the information from the list to an excel document such that each field in the dictionary is a column. 

#### Google's Project Sunroof

#### Zillow


## Usage Instructions

## Sources 

## Contact 
