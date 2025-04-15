import requests
import time
import openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
ws = wb.active

header = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

for row in range(2,ws.max_row+1):
    try:
        url = ws.cell(row=row, column=7).value
        response = requests.get(url, headers=header, timeout=10)
        response.raise_for_status()  # raises exception for 4xx/5xx errors
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
    time.sleep(30)