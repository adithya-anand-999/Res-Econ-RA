from coordinates import get_coordinates
from capacity_factor import get_capacity_factor
from roof_space import get_roof_space
from zillow_url import get_zillow_url
# from zillow_data import get_zillow_data
# from zillow_data import get_snapshot_id

import openpyxl
import asyncio
import time


def get_data(given_excel_path, new_excel_name=None):
    wb = openpyxl.load_workbook(given_excel_path)
    ws = wb.active

    num_rows = ws.max_row

    for row in range(205,num_rows+1):
        addr = ws.cell(row=row, column=1).value
        if addr:
            print(addr)
            lat, lon = get_coordinates(addr)
            ws.cell(row=row, column=8, value=get_capacity_factor(lat,lon))
            ws.cell(row=row, column=9, value=asyncio.run(get_roof_space(addr.split(" ")[0],lat,lon)))
            url = get_zillow_url(addr)
            ws.cell(row=row, column=10, value=url)
            # zillow_data = get_zillow_data(get_snapshot_id(url))
            # if not zillow_data: continue
            # for i,point in enumerate(zillow_data.values()):
            #     ws.cell(row=row, column=11+i, value=point if point else "None")
            wb.save(given_excel_path)
            time.sleep(1)
        print(f"Row {row} completed")
    print("Done updating Excel file.")



get_data("./given_excel.xlsx")