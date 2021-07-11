from math import sin, cos, asin, acos, radians, degrees
from Util import get_coordinates


class SunElevationAzimuth:
    """ Performs various calculations to find the Sun's current elevation and
    azimuth given a date, time with timezone, and coordinates.

    Attributes:
        date : datetime
            the current timezone aware local date
        day_of_year : int
            the current integer day of the year
        _local_solar_time : float
            the local solar time in hours
        latitude : float
            local latitude
        longitude : float
            local longitude
        _declination : float
            the Sun's declination angle
        _hra : float
            the hour angle
        _elevation : float
            the Sun's current elevation
        _azimuth : float
            the Sun's current azimuth

    Methods:
        get_elevation():
            returns the Sun's current elevation.
        get_azimuth():
        returns the Sun's current azimuth.
    """

    def __init__(self, dt):
        """
        :param dt: a DatesAndTimes object
        """
        self.date = dt.get_date()
        self.day_of_year = dt.get_day_of_year()
        self._local_solar_time = dt.get_local_solar_time()
        self.latitude, self.longitude = get_coordinates()
        self._declination = 0.0
        self._hra = 0.0
        self._elevation = 0.0
        self._azimuth = 0.0

        self._declination_angle()
        self._hour_angle()
        self._sun_elevation()
        self._sun_azimuth()

    def _declination_angle(self):
        """ Calculates the Sun's current declination angle.
        Result is in degrees.
        """
        self._declination = 23.45 * sin(radians(360 * (284 + self.day_of_year) / 365))

    def _hour_angle(self):
        """ Calculates the current hour angle. The hour angle is the number of
        degrees the sun has moved across the sky.
        """
        earth_hourly_rotation = 15
        self._hra = earth_hourly_rotation * (self._local_solar_time - 12)

    def _sun_elevation(self):
        """ Calculates the Sun's current elevation.
        Result is in degrees.
        """
        term_1 = sin(radians(self._declination)) * sin(radians(self.latitude))
        term_2 = cos(radians(self._declination)) * cos(radians(self.latitude)) * cos(radians(self._hra))
        self._elevation = asin(term_1 + term_2)
        self._elevation = degrees(self._elevation)

    def _sun_azimuth(self):
        """ Calculates the Sun's current azimuth.
        Result is in degrees.
        """
        numerator = (sin(radians(self._declination)) * cos(radians(self.latitude))) \
            - (cos(radians(self._declination)) * sin(radians(self.latitude))
                * cos(radians(self._hra)))
        denominator = cos(radians(self._elevation))
        self._azimuth = acos(numerator / denominator)
        self._azimuth = 360 - degrees(self._azimuth)

    def get_elevation(self):
        return self._elevation

    def get_azimuth(self):
        return self._azimuth
