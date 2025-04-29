from config import API_KEY
import googlemaps
import openpyxl


def get_lat_long_google(address, api_key):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    return (None)

wb = openpyxl.load_workbook('./res-econ_RA_data.xlsx')
ws = wb.active

for row in range(2,5):

    addr = ws.cell(row=row, column=1).value

    print(get_lat_long_google(addr, API_KEY))





