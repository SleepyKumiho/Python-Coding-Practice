import googlemaps
import openpyxl
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

def geocode_file_excel(input_file_name, output_file_name, key = api_key):
    input_wb = openpyxl.load_workbook(filename = input_file_name)
    input_ws = input_wb.active
    output_wb = openpyxl.Workbook()
    output_ws = output_wb.active

    row_num = 1
    for row in input_ws.values:
        print(row[1])
        output_ws.cell(row = row_num, column = len(row)+1, value = row[0])
        row_num += 1
    output_wb.save(output_file_name)

    return 1

def geocode_file_csv(input_file_name, output_file_name, key = api_key):
    None


if __name__ == '__main__':
    #address = "Jeremy Ranch Park & Ride, Park City, UT"
    #print(geocode_from_address(address))
    geocode_file_excel("../../../Desktop/test.xlsx", "../../../Desktop/output.xlsx", 5)
