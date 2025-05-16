# Residential Solar PV Data Collection 
API and web scraping data collection conducted with the Department of Resources Economics at the University of Massachusetts — Amherst. 

## Overview
The attached code gathers data from a list of addresses across three different websites: NREL's PVWatts Calculator, Google's Project Sunroof, and Zillow.  The code for extracting the data from each website is split into individual files, however, the code can be run in its entirety from data.py.  

## Usage Instructions
Below please find the setup and methodology implemented for each website.  Please see inline comments for detailed instructions on running the code. 

### Setup

#### API Key Configurations 
In total, the code requires four API keys: one to interact with Google services (Maps, Project Sunroof, Custom Search Engine), an additional key for the Google Custom Search Engine to identify the specific search engine, one for PVWatts, and one for Bright Data.  We store each key in a config.py file to maintian privacy.

#### Coordinates
PVWatts and Project Sunroof both utilize coordinates to access a locations associated data.  Thus, we first developed the function get_coordinates(), which converts the list of addresses to coordinates via the Google Maps API.

### Wesbites

#### NREL's PVWatts Calculator
NREL offers a free, public API for their PVWatts calculator, we used thier API in our function, get_capacity_factor().  The function get_capacity_factor() takes in latitude and longitude coordinates, determined by get_coordinates(), to query the PVWatts API and return the value associated witht the DC Capacity Factor.  Please see capacity_factor.py for complete instructions. 

#### Google's Project Sunroof

#### Zillow

## Sources 

## Contact 
