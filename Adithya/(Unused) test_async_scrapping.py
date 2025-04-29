import os
import nest_asyncio
nest_asyncio.apply()

from requests_html import AsyncHTMLSession
from pyppeteer import launch
import asyncio

# Set the correct path to Chrome executable
os.environ["PYPPETEER_EXECUTABLE_PATH"] = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

asession = AsyncHTMLSession()

async def test():
    r = await asession.get("https://example.com")
    
    # Force using existing Chrome installation
    r.browser = await launch(
        executablePath=os.environ["PYPPETEER_EXECUTABLE_PATH"],  # Use the environment variable for chrome path
        headless=True,  # Run in headless mode (without opening browser window)
        args=["--no-sandbox"]
    )
    
    await r.html.arender()
    print(r.html.html[:500])  # Print part of the HTML

asyncio.run(test())
