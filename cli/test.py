import unittest
from datetime import datetime

from date import get_days_difference, get_date_obj


class DateCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.date_test_data = [{'start_date': '02/06/1983', 'end_date': '22/06/1983'},
                               {'start_date': '04/07/1984', 'end_date': '25/12/1984'},
                               {'start_date': '03/08/1983', 'end_date': '03/01/1989'}]

    def test_cli_datetime(self):
        # Days difference will include start day count, so we need to subtract it by 1
        # in order to exclude partial start day and end day.
        self.assertEqual(get_days_difference(get_date_obj(self.date_test_data[0]['start_date']),
                                             get_date_obj(self.date_test_data[0]['end_date'])) - 1, 19)
        self.assertEqual(get_days_difference(get_date_obj(self.date_test_data[1]['start_date']),
                                             get_date_obj(self.date_test_data[1]['end_date'])) - 1, 173)
        self.assertEqual(get_days_difference(get_date_obj(self.date_test_data[2]['start_date']),
                                             get_date_obj(self.date_test_data[2]['end_date'])) - 1, 1979)

    def test_compare_python_datetime(self):
        """Compare days  difference with cli date module date obj and python date obj"""
        start_date = self.date_test_data[0]['start_date']
        end_date = self.date_test_data[0]['end_date']

        start_date_obj = datetime.strptime(start_date, '%d/%m/%Y').date()
        end_date_obj = datetime.strptime(end_date, "%d/%m/%Y").date()

        self.assertEqual(
            get_days_difference(get_date_obj(start_date), get_date_obj(end_date)),
            (end_date_obj - start_date_obj).days
        )


if __name__ == "__main__":
    unittest.main()
