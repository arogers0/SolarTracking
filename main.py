from pysolar.solar import *
import warnings
from DatesAndTimes import *
from SunElevationAzimuth import *
from Util import get_coordinates


def main():

    d = DatesAndTimes()
    sol = SunElevationAzimuth(d)
    date = d.get_date()
    latitude, longitude = get_coordinates()

    print(sol.get_elevation())
    print(sol.get_azimuth())

    print_info(date, latitude, longitude)


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
