# required libraries to install for function get_roof_space
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# required libraries for testing function, uncomment if running testing block at end. 
# import asyncio
# import openpyxl


# This function is written asynchronously as the google solar website is dynamic. Dynamic means the website takes some time to fully load, as such a delay exists 
# between initial website query and successful data collection. By writing our function asynchronously we are able to speed up data collection by querying the website 
# for a new address in the time we wait for the previous address to load with data. 

# We decided to use the playwright library for this as they offer modern support for chrome browsers allowing us to run our code across Windows and Mac. 


async def get_roof_space(addr_num,lat,lon): # addr_num=number of the street address, lat=lat of address, lon=lon of address
    url = f"https://sunroof.withgoogle.com/building/{str(round(float(lat),4))}/{str(round(float(lon),4))}/#?f=buy"  # google solar website url, we query using the lat and lon of an address

    async with async_playwright() as p: # opens the asynchronous portion of our code
        # Scrapping website
        browser = await p.chromium.launch(headless=True) # creates a browser instance, here we use a chrome browser 
        page = await browser.new_page() # opens a new tab in our browser 
        await page.goto(url, timeout=30000) # navigates to our google solar website url, timeout shows that it can take up to 30 seconds to navigate to the url, although should never take this long
        html = await page.content() # waits for the dynamic website to fully load, then scrapes all the html. This html contains our roof_space data point. 
        await browser.close() # as scraping is complete we can close the browser and tab we created previously 
        soup = BeautifulSoup(html, "html.parser") # optional, using BeautifulSoup to make the html cleaner, helped when we logged html to find roof_space within html. 

        # Checking if address numbers match
        inp = soup.find("input", attrs={"aria-label": True}) # first place address at this lat and lon could be
        if not inp: inp = soup.find("input", attrs={"placeholder": True}) # second place address at this lon and lat could be
        if inp: # if we found either element it means we have an address to check, if not else block runs
            address = inp.get("aria-label") or inp.get("placeholder") # data fields of where address is located
            if addr_num not in address.split(" ")[0]: return "None" # check if it matches the passed arg addr_num
        else: # will run if we could not find an address in the html
            print("Couldn’t find the address input in the page.")
            return "None"
        
        # roof_space data collection
        upper_li = soup.find("li", attrs={"ng-if": "$ctrl.derivedValues.getMaxArrayAreaSqft()"}) # In the html roof_space found within this element
        if upper_li: # if it exists continue
            data_div = upper_li.find("div", class_="panel-fact-text md-body") # within upper_li roof_space found within this element
            if data_div: # if it exists continue
                val = data_div.get_text(strip=True).split()[0] # roof_space is the first element within data_div, so we grab the value
                return(val) # lastly we return the value 
            else:
                print("Inner data div not found.")
                return("Inner data div not found.")
        else: # first container does not exist so we can return
            print("Upper div with specified ng-if not found.")
            return("Upper div with specified ng-if not found.")


# code to test our function, make sure to uncomment above library imports to run
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active
# test_lat, test_lon = ws.cell(row=4, column=2).value, ws.cell(row=4, column=3).value
# test_addr = ws.cell(row=4, column=1).value
# test_data = data = asyncio.run(get_roof_space(test_addr.split(" ")[0],test_lat,test_lon))
# print(test_data)
