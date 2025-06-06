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

1. Navigate to https://console.cloud.google.com/apis/library?inv=1&invt=AbycLQ. This is the website for all Google APIs and other services, here is where we will make our Google API key. 

2. Sign in/Create an account. You will be asked to provide a payment method although you won't be charged as each new account is given $300 in free credits. Of these credits our code will only use a few cents. 

3. On this page https://console.cloud.google.com/apis/library search for the following API services and click enable, “Geocoding API” and “Custom Search API”. An enable button will appear once you search for an API service. 

4. Navigate to https://console.cloud.google.com/apis/credentials and at the top bar click the “Create Credentials” dropdown. Then select API key. This will show a card with your Google API key, store this for use later in config.py. 

### Google Custom Search Engine Parameter 

1. This website https://developers.google.com/custom-search/docs/tutorial/creatingcse contains the steps to make a custom Google Search Engine to collect zillow urls for an address.

2. Click the hyperlinked [“control panel”](https://programmablesearchengine.google.com/controlpanel/create). 

3. Name the search engine anything, e.g. zillow_url_collection. 
4. Under the heading, “What to search?” paste this link: “https://www.zillow.com/” in the input box, this will make sure our search engine only looks for Zillow urls for a given query. After pasting the link click the “add” button. 

5. Click the “create” button after completing the bot check. 

6. You should now see three lines of code on your screen, the first line should read something like this: <script async src="https://cse.google.com/cse.js?cx=xxxxxxxxxxxxxxxx"> (I have replaced the cx parameter with x’s as a placeholder, you should see a string of numbers and letters). The cx parameter is what we need. Store this cx parameter, it will be used in config.py later. 

### Bright Data

1. From [Bright Data’s home page](https://brightdata.com/), on the top right corner, click login 

2. After signing in, on the bottom left corner of the left menu, click “Account Settings”

3. In the API keys section, store the key for use in config.py, this is your Bright Data API Key


## Contact

Adithya Anand 
adithyaanand817@gmail.com 

Elizabeth O'Brien 
obrien.elizabethkennedy@gmail.com 

