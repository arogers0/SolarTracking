from math import sin, cos, asin, acos
from DatesAndTimes import *
from Util import get_coordinates


class SunElevationAzimuth:

    def __init__(self, dt):
        self.date = dt.get_date()
        self.day_of_year = dt.get_day_of_year()
        self._local_solar_time = dt.get_local_solar_time()
        self.latitude, self.longitude = get_coordinates()
        self._declination = 0
        self._hra = 0
        self._elevation = 0
        self._azimuth = 0

        self._declination_angle()
        self._hour_angle()
        self._sun_elevation()
        self._sun_azimuth()

    def _declination_angle(self):
        # self._declination = 23.45 * sin((360 / 365) * (self.day_of_year - 81))
        self._declination = 23.45 * sin(radians(360 * (284 + self.day_of_year) / 365))

    def _hour_angle(self):
        self._hra = 15 * (self._local_solar_time - 12)

    def _sun_elevation(self):
        term_1 = sin(self._declination) * sin(self.latitude)
        term_2 = cos(self._declination) * cos(self.latitude) * cos(self._hra)
        self._elevation = asin(term_1 + term_2)

    def _sun_azimuth(self):
        numerator = (sin(radians(self._declination)) * cos(radians(self._declination))) \
                    - (cos(radians(self._declination)) * cos(self.latitude) * cos(self._hra))
        denominator = cos(radians(self._elevation))
        self._azimuth = acos(numerator / denominator)

    def get_elevation(self):
        return self._elevation

    def get_azimuth(self):
        return self._azimuth
