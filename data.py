from coordinates import get_coordinates
from capacity_factor import get_capacity_factor
from roof_space import get_roof_space
from zillow_url import get_zillow_url
from zillow_data import get_zillow_data

import openpyxl



def get_data(given_excel_path, new_excel_name):
    wb = openpyxl.load_workbook(given_excel_path)
    ws = wb.active

    num_rows = ws.max_row

    for row in range(2,num_rows):
        addr = ws.cell(row=row, column=1).value
        lat, long = 

    # for row in range(2,211):
#     addr = ws.cell(row=row, column=1).value
#     # print(addr_num)
#     lat = ws.cell(row=row, column=2).value
#     long = ws.cell(row=row, column=3).value
#     data = asyncio.run(scrape_roof_space(addr.split(" ")[0],lat,long))
#     print(f"{addr} → {data}")
#     ws.cell(row=row, column=5, value=data)
#     wb.save('res-econ_RA_data.xlsx')
#     time.sleep(1)
# print("Done updating Excel file.")