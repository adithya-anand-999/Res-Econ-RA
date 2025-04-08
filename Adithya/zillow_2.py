from googlesearch import search
import requests

def get_zillow_url(address):
    query = f'site:zillow.com "{address}"'
    for url in search(query, num_results=5):
        if "zillow.com/homedetails" in url:
            return url.split('?')[0]  # clean up tracking params
    return None



