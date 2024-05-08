import googlemaps
from openpyxl import Workbook
import csv

api_key = ""

def geocode_from_address(address, key = api_key):
    """
    Use the googlemaps API to geocode an address (turn a physical address into latitude and longitude)

    Input:
    address (str): A human readable address
    key (str): A Google Maps Platform API key 

    Return:
    (dict): a dictionary containing the latitude and longitude as decimal values 
    """
    gmaps = googlemaps.Client(key = key)
    geocode_result = gmaps.geocode(address)

    # If the address cannot be geocoded, just return None 
    try:
        return geocode_result[0]["geometry"]["location"]
    except:
        return None

if __name__ == '__main__':
    address = "Jeremy Ranch Park & Ride, Park City, UT"
    print(geocode_from_address(address))
