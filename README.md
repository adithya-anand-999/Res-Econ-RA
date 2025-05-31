# Residential Solar PV Data Collection 
*Residential solar PV data collection conducted in support of research at the University of Massachusetts — Amherst, Department of Resource Economics.*  

## Overview
The attached code gathers various data points for a list of addresses across three different websites: NREL's PVWatts Calculator, Google's Project Sunroof, and Zillow. The code for extracting the data from each website is split into individual files, however, the code can be run, and data collected, from data.py.

## Usage Instructions
Below please find the setup and methodology implemented for each website.  Please see inline comments for detailed instructions on running the code. 

## Setup

In total, the code requires four keys: one for PVWatts, one to interact with Google services (Maps, Project Sunroof, Custom Search Engine), an additional key for the Google Custom Search Engine to identify the specific search engine, and one for Bright Data. We store each key in a config.py file to maintain privacy. 

### Libraries to Install
Run the below two commands in a terminal environment before running the code. This will install all the external libraries our code requires. If you don’t have pip installed on your machine you can follow this tutorial here, it has instructions for both Windows, Mac, and Linux https://pip.pypa.io/en/stable/installation/. 
  
```
pip install requests openpyxl beautifulsoup4 playwright googlemaps
playwright install
```


### PVWatts API Key

1. From [NREL’s PVWatts Calculator](https://pvwatts.nrel.gov/pvwatts.php), click "Help", then "About", within the Information for Developers subheading, click the hyperlinked "[PVWatts V8 API](https://developer.nrel.gov/docs/solar/pvwatts/)" to access the [Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/)

2. From the top menu of [NREL’s PVWatts V8 API Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/), select "[Key Signup](https://developer.nrel.gov/signup )" and enter your information to receive an API key via email

3. Upon receipt of the emailed API key, please store the key in config.py as a variable named PV_API_KEY

4. For further details regarding the API used, return to the top menu of [NREL’s PVWatts V8 API Developer Network page](https://developer.nrel.gov/docs/solar/pvwatts/), select "[APIs & Documentation](https://developer.nrel.gov/docs/)", select "Solar", then "PVWatts", the present code uses [PVWatts V8](https://developer.nrel.gov/docs/solar/pvwatts/v8/), the current version of the PVWatts API

### Google API Key

### Google Custom Search Engine Parameter 

### Bright Data


## Contact 
