from unittest import TestCase
from SunElevationAzimuth import *
from DatesAndTimes import *
from pysolar.solar import *
import warnings


class TestSunElevationAzimuth(TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", '.*leap seconds.*')
        lat, lon = get_coordinates()
        dt = DatesAndTimes()
        sol = SunElevationAzimuth(dt)
        self.calc_elev = sol.get_elevation()
        self.calc_azimuth = sol.get_azimuth()
        self.elev = get_altitude(lat, lon, dt.get_date())
        self.azimuth = get_azimuth(lat, lon, dt.get_date())

    def test__sun_elevation(self):
        """
        Check to see that the integer part of the calculated elevation and
        PySolar elevation are the same.
        """
        self.assertAlmostEqual(self.calc_elev, self.elev, 0)

    def test__sun_azimuth(self):
        """
        Check to see that the integer part of the calculated azimuth and
        PySolar azimuth are the same.
        """
        self.assertAlmostEqual(self.calc_azimuth, self.azimuth, 0)
