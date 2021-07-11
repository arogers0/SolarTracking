from geopy.geocoders import Nominatim


def get_coordinates(lat=True, lon=True):
    """ Get rough coordinates from city and country/state.

    :return: a geopy location
    """
    geolocator = Nominatim(user_agent="my_user_agent")
    city = "Merrick"
    country = "NY"
    loc = geolocator.geocode(city + ',' + country)
    if lat is True and lon is True:
        return loc.latitude, loc.longitude
    elif lat is True and lon is False:
        return loc.latitude
    elif lat is False and lon is True:
        return loc.longitude
    else:
        return
