# Residential Solar PV Data Collection 

## Overview
Residential solar PV data collection conducted in support of research at the University of Massachusetts — Amherst, Department of Resource Economics.  The attached code gathers various data points for a list of addresses across three different websites: NREL's PVWatts Calculator, Google's Project Sunroof, and Zillow. The code for extracting the data from each website is split into individual files, however, the code can be run, and data collected, from data.py.

## Usage Instructions
Below please find the setup and methodology implemented for each website.  Please see inline comments for detailed instructions on running the code. 

## Setup

In total, the code requires four keys: one for PVWatts, one to interact with Google services (Maps, Project Sunroof, Custom Search Engine), an additional key for the Google Custom Search Engine to identify the specific search engine, and one for Bright Data. We store each key in a config.py file to maintain privacy. 

#### PVWatts API Key

1. From [NREL’s PVWatts Calculator](https://pvwatts.nrel.gov/pvwatts.php), click Help, then About, within the Information for Developers subheading, click the hyperlinked [PVWatts V8 API](https://developer.nrel.gov/docs/solar/pvwatts/) to access the [Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/)

2. From the top menu of [NREL’s PVWatts V8 API Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/), select [Key Signup](https://developer.nrel.gov/signup ) and enter your information to receive an API key via email

3. Upon receipt of the emailed API key, please store the key in config.py as a variable named PV_API_KEY

4. For further details regarding the API used, return to the top menu of [NREL’s PVWatts V8 API Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/), select [APIs & Documentation](https://developer.nrel.gov/docs/), select [Solar](https://developer.nrel.gov/docs/solar/), then [PVWatts](https://developer.nrel.gov/docs/solar/pvwatts/), the attached code currently uses [PVWatts V8](https://developer.nrel.gov/docs/solar/pvwatts/v8/), the current version of the PVWatts API

#### Google API Key

#### Google Custom Search Engine Parameter 

#### Bright Data


## Contact 
