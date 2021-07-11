import datetime
from math import sin, cos, tan, asin, acos, atan, radians
from Util import get_coordinates


class DatesAndTimes:

    def __init__(self):
        self._date = datetime.datetime.now().astimezone()
        self._day_of_year = datetime.datetime.now().timetuple().tm_yday
        self._local_time_hours = 0
        self._lstm = 0
        self._eot = 0
        self._tc = 0
        self._lst = 0

        self._calc_local_time_hours()
        self._local_std_time_meridian()
        self._equation_of_time()
        self._time_correction_factor()
        self._local_solar_time()

    def _calc_local_time_hours(self):
        hour_component = self._date.hour
        minute_component = self._date.minute / 60
        second_component = self._date.second / 3600
        self._local_time_hours = hour_component + minute_component + second_component

    def _local_std_time_meridian(self):
        local_hour = datetime.datetime.now().hour
        utc_hour = datetime.datetime.utcnow().hour
        delta_t = utc_hour - local_hour

        # Handle Daylight Savings
        if datetime.date(self._date.year, 3, 14) < datetime.date.today() < datetime.date(self._date.year, 11, 7):
            delta_t += 1

        self._lstm = 15 * -delta_t

    def _equation_of_time(self):
        b = (360 / 365) * (self._day_of_year - 1)

        self._eot = 229.2 * (0.000075 + 0.001868 * cos(radians(b)) - 0.032077 * sin(radians(b))-
                    0.014615 * cos(radians(2 * b)) - 0.04089 * sin(radians(2 * b)))

        print(self._eot)

    def _time_correction_factor(self):
        longitude = get_coordinates(False, True)
        self._tc = 4 * (longitude - self._lstm) + self._eot
        print(self._tc)

    def _local_solar_time(self):
        self._lst = self._local_time_hours + (self._tc / 60)
        print(self._lst)

    def get_date(self):
        return self._date

    def get_day_of_year(self):
        return self._day_of_year

    def get_local_solar_time(self):
        return self._lst
