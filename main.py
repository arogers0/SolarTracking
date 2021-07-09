from geopy.geocoders import Nominatim
from pysolar.solar import *
import datetime
import warnings


def main():

    latitude, longitude = get_location_coordinates()

    date = datetime.datetime.now().astimezone()

    print_info(date, latitude, longitude)


def get_location_coordinates():
    """ Get rough coordinates from city and country/state.

    :return: a geopy location
    """
    geolocator = Nominatim(user_agent="my_user_agent")
    city = "Merrick"
    country = "NY"
    loc = geolocator.geocode(city + ',' + country)
    return loc.latitude, loc.longitude


def print_info(date, lat, lon):
    """ Prints user's location coordinates, and Sun's elevation and azimuth.

    :param date: Timezone-aware datetime
    :param lat: latitude coordinate
    :param lon: longitude coordinate
    """
    print("Latitude is:".ljust(16), lat, "\nLongitude is:".ljust(16), lon)
    print("Sun Elevation:".ljust(16), get_altitude(lat, lon, date))
    print("Sun Azimuth:".ljust(16), get_azimuth(lat, lon, date))


if __name__ == "__main__":
    warnings.filterwarnings("ignore", '.*leap seconds.*')
    main()
