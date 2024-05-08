import googlemaps


def geocode_from_address(address, key = api_key):
    gmaps = googlemaps.Client(key = key)
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]["geometry"]["location"]

if __name__ == '__main__':
    address = "Jeremy Ranch Park & Ride, Park City, UT"
    print(geocode_from_address(address))
