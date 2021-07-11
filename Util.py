from geopy.geocoders import Nominatim
from pysolar.solar import *


def get_coordinates(lat=True, lon=True):
    """ Get rough coordinates from city and country/state.

    :param lat: Boolean that specifies whether or not to return latitude.
    :param lon: Boolean that specifies whether or not to return longitude.
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


def print_info(date, lat, lon, sol):
    """ Prints user's location coordinates, and Sun's elevation and azimuth.

    :param date: Timezone-aware datetime
    :param lat: latitude coordinate
    :param lon: longitude coordinate
    :param sol: SunElevationAzimuth object
    """
    print("From PySolar:")
    print("Latitude is:".ljust(16), lat, "\nLongitude is:".ljust(16), lon)
    print("Sun Elevation:".ljust(16), get_altitude(lat, lon, date))
    print("Sun Azimuth:".ljust(16), get_azimuth(lat, lon, date))

    print("\nCalculated Results:")
    print("Sun Elevation:".ljust(16), sol.get_elevation())
    print("Sun Azimuth:".ljust(16), sol.get_azimuth())
