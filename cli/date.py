# Module to define Date class and get difference of dates excluding start and end date
import re


class Date:
    def __init__(self, year, month, day):
        """Initialize year, month and day provided as arguments"""
        self._year = year
        self._month = month
        self._day = day

    # Conversions to string
    def __repr__(self):
        """Convert to formal string for representation"""
        return f'{self._day}/{self._month}/{self._year}'

    # Read-only field accessors
    @property
    def year(self):
        """year (1-9999)"""
        return self._year

    @property
    def month(self):
        """month (1-12)"""
        return self._month

    @property
    def day(self):
        """day (1-31)"""
        return self._day


# -1 is a placeholder for indexing purposes.
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _is_leap(year):
    """year -> 1 if leap year, else 0."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    assert 1 <= month <= 12, "Month should be in range 1-12"
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]


def _total_leap_years(year):
    """Calculate total leap years till provided year"""
    assert 1 <= year <= 9999, "Year should be in range 1-9999"
    # Leap year is a multiple of 4 or 400 but not a multiple of 100
    return int(year / 4) - int(year / 100) + int(year / 400)


def _get_days_till_date(date: Date):
    """Count number of days before provided date"""
    # Total number of days till provided date year
    days = date.year * 365

    # Add days for months in provided date year excluding current month
    for i in range(1, date.month):
        days += _days_in_month(date.year, i)

    # Add leap years count and days in current month.
    # Excluding current year as it is calculated already in above step
    days += _total_leap_years(date.year - 1) + date.day
    return days


def is_date_valid(date_str):
    """Regex to validate date string in format and range 01/01/1901 - 31/12/2999"""
    if re.match(r"^((0[1-9]|[12]\d|3[01])\/(0[1-9]|1[0-2])\/([1][9][0][1-9]|[1][9][1-9]\d|2\d\d\d))$", date_str):
        return True
    return False


def get_date_obj(date_str):
    """Convert date str to Date obj"""
    values = list(map(int, date_str.split('/')))
    return Date(values[2], values[1], values[0])


def get_days_difference(start_date: Date, end_date: Date):
    """Count number of days between start date and end date"""
    # Calculate number of days till start date and end date
    n1 = _get_days_till_date(start_date)
    n2 = _get_days_till_date(end_date)

    # Days difference including start date but not the end date
    return n2 - n1
