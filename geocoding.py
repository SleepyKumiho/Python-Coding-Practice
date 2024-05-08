import googlemaps

api_key = ""

def geocode_from_address(address, key = api_key):
    gmaps = googlemaps.Client(key = key)
    geocode_result = gmaps.geocode(address)
    print(geocode_result)
    return geocode_result

if __name__ == '__main__':
    address = "Jeremy Ranch Park & Ride, Park City, UT"
    geocode_from_address(address)
