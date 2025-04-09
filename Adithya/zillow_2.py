from googlesearch import search
import pandas as pd
import time

def get_zillow_url(address):
    query = f'site:zillow.com "{address}"'
    for url in search(query, num_results=5):
        if "zillow.com/homedetails" in url:
            return url.split('?')[0]  # clean up tracking params
    return None

# Load the addresses from the Excel file.
df = pd.read_excel('./res-econ_RA_data.xlsx')  
addresses = list(df.iloc[:, 0].dropna())

# Open the file for writing URLs.
with open("zillow_urls.txt", "a") as outfile:
    # You can adjust the slice to go through all addresses if needed.
    for address in addresses[11:]:
        print(f"Searching: {address}")
        url = get_zillow_url(address)
        print(f"→ {url}")
        
        # Write the URL and insert a newline.
        outfile.write(f"{url}\n")
        
        # Sleep for 1 second between requests.
        time.sleep(1)
