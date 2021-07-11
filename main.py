import warnings
from DatesAndTimes import *
from SunElevationAzimuth import *
from Util import get_coordinates, print_info


def main():
    """Run this to calculate the Sun's current elevation and azimuth."""

    d = DatesAndTimes()
    sol = SunElevationAzimuth(d)
    date = d.get_date()
    latitude, longitude = get_coordinates()

    print_info(date, latitude, longitude, sol)


if __name__ == "__main__":
    warnings.filterwarnings("ignore", '.*leap seconds.*')
    main()
