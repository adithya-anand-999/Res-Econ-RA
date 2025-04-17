import os

import nest_asyncio
nest_asyncio.apply()

from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import asyncio
# import pyppeteer.errors
os.environ["PYPPETEER_EXECUTABLE_PATH"] = r" C:\Program Files\Google\Chrome\Application\chrome.exe"

asession = AsyncHTMLSession()

async def scrape_roof_space(lat,lon):
    url = f"https://sunroof.withgoogle.com/building/{str(round(float(lat),4))}/{str(round(float(lon),4))}/#?f=buy"

    try:
        response = await asession.get(url)
        await response.html.arender(timeout=20)
        soup = BeautifulSoup(response.html.html, "html.parser")
        print(soup)

        upper_li = soup.find("li", attrs={"ng-if": "$ctrl.derivedValues.getMaxArrayAreaSqft()"})
        if upper_li:
            data_div = upper_li.find("div", class_="panel-fact-text md-body")
            if data_div:
                val = data_div.get_text(strip=True).split()[0]
                print(val)
                return(val)
            else:
                print("Inner data div not found.")
                return("Inner data div not found.")
        else:
            print("Upper div with specified ng-if not found.")
            return("Upper div with specified ng-if not found.")
    except Exception as e:
        print(f"Uncaught error {e} occurred")
        return("None")

asyncio.run(scrape_roof_space("42.3420389", "-72.4823318"))

