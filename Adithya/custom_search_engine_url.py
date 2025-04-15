# This is a code file for working on the custom search engine google API to create a more robust system for URL collections. 
import requests
import openpyxl
import time

from config import API_KEY
from config import CX


def custom_SE(addr, key=API_KEY, cx=CX):
    url=f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={addr}"
    try:
        response = requests.get(url=url).json()
        data = response['items'][0]['link']
        print(f"{addr} → {data}")
        return(data)
    except Exception as err:
        print(f"{err} occurred when processing address: {addr}")
        return None


# simple tests of the custom_SE function
# addrs = ["6 STANDISH CIR, ANDOVER, MA, 01810", "150 TRAINCROFT ST, MEDFORD, MA, 02155"]
# custom_SE(addrs[1])

# code updates excel file res-econ_RA_data.xlsx. Commented out as no reason to run code more than once. All urls have been collected.
# wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
# ws = wb.active

# for row in range(1,ws.max_row+1):
#     address = ws.cell(row=row, column=1).value
#     url = custom_SE(address)
#     ws.cell(row=row, column=7, value=url)
#     wb.save('res-econ_RA_data.xlsx')
#     time.sleep(1)

# print("Done updating Excel file.")
