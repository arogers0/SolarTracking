import datetime
from math import sin, cos, radians
from Util import get_coordinates


class DatesAndTimes:
    """ Performs various date and time calculations.

    Attributes:
        _date : datetime
            a timezone aware date
        _day_of_year : int
            the integer day of the year for today
        _local_time_hours : float
            current time of day represented in hours
        _lstm : float
            the local standard time meridian
        _eot : float
            the equation of time result
        _tc : float
            the time correction factor
        _lst : float
            the local solar time in hours

    Methods:
        get_date():
            returns the current timezone aware local date.
        get_day_of_year():
            returns the current integer day of the year.
        get_local_solar_time():
            returns the current local solar time in hours.
    """

    def __init__(self):
        self._date = datetime.datetime.now().astimezone()
        self._day_of_year = datetime.datetime.now().timetuple().tm_yday
        self._local_time_hours = 0.0
        self._lstm = 0.0
        self._eot = 0.0
        self._tc = 0.0
        self._lst = 0.0

        self._calc_local_time_hours()
        self._local_std_time_meridian()
        self._equation_of_time()
        self._time_correction_factor()
        self._local_solar_time()

    def _calc_local_time_hours(self):
        """Uses date information to compute a float type where minutes and
        seconds are fractions of an hour.
        """
        hour_component = self._date.hour
        minute_component = self._date.minute / 60
        second_component = self._date.second / 3600
        self._local_time_hours = hour_component + minute_component + second_component

    def _local_std_time_meridian(self):
        """Calculates the meridian for the local timezone.
        Result is in degrees.
        """
        local_hour = datetime.datetime.now().hour
        utc_hour = datetime.datetime.utcnow().hour
        delta_t = utc_hour - local_hour

        # Handle Daylight Savings
        #if datetime.date(self._date.year, 3, 14) < datetime.date.today() < datetime.date(self._date.year, 11, 7):
        #    delta_t += 1

        self._lstm = -15 * delta_t

    def _equation_of_time(self):
        """Calculates the time difference between local time and solar time.
        Result is in minutes.
        """
        b = (360 / 365) * (self._day_of_year - 1)

        self._eot = 229.2 * (0.000075 + 0.001868 * cos(radians(b)) - 0.032077
                             * sin(radians(b)) - 0.014615 * cos(radians(2 * b))
                             - 0.04089 * sin(radians(2 * b)))

    def _time_correction_factor(self):
        """Additional time correction that accounts for variations in longitude
        within a timezone.
        Result is in minutes.
        """
        longitude = get_coordinates(False, True)
        self._tc = 4 * (longitude - self._lstm) + self._eot

    def _local_solar_time(self):
        """Calculates the local solar time by summing the local time and time
        correction factor (in hours).
        """
        self._lst = self._local_time_hours + (self._tc / 60)

    def get_date(self):
        return self._date

    def get_day_of_year(self):
        return self._day_of_year

    def get_local_solar_time(self):
        return self._lst
