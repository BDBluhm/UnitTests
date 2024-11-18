import unittest
from datetime import datetime

def validate_date(date_text):
    if not date_text:
        return False
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        return start <= end
    except ValueError:
        return False

class TestInputValidation(unittest.TestCase):

    def test_symbol_valid(self):
        """Test valid stock symbol."""
        valid_symbols = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN", "META", "IBM"]
        for symbol in valid_symbols:
            self.assertTrue(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

    def test_symbol_invalid(self):
        """Test invalid stock symbol."""
        invalid_symbols = ["aapl", "123ABC", "TOOLONGSYMBOL", "A!@#$", ""]
        for symbol in invalid_symbols:
            self.assertFalse(symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7)

    def test_chart_type_valid(self):
        """Test valid chart types."""
        valid_chart_types = ['1', '2']
        for chart_type in valid_chart_types:
            self.assertTrue(chart_type in ['1', '2'])

    def test_chart_type_invalid(self):
        """Test invalid chart types."""
        invalid_chart_types = ['0', '3', '12', 'A', '', None]
        for chart_type in invalid_chart_types:
            self.assertFalse(chart_type in ['1', '2'])

    def test_time_series_valid(self):
        """Test valid time series."""
        valid_time_series = ['1', '2', '3', '4']
        for time_series in valid_time_series:
            self.assertTrue(time_series in ['1', '2', '3', '4'])

    def test_time_series_invalid(self):
        """Test invalid time series."""
        invalid_time_series = ['0', '5', '12', 'A', '', None]
        for time_series in invalid_time_series:
            self.assertFalse(time_series in ['1', '2', '3', '4'])

    def test_start_date_valid(self):
        """Test valid start dates."""
        valid_dates = ["2024-01-01", "1990-12-31", "2023-05-15"]
        for date in valid_dates:
            self.assertTrue(validate_date(date))

    def test_start_date_invalid(self):
        """Test invalid start dates."""
        invalid_dates = [
            "2024-02-30",
            "2024-13-01",
            "2024-01-32",
            "invalid-date"
        ]
        for date in invalid_dates:
            self.assertFalse(validate_date(date))

    def test_end_date_valid(self):
        """Test valid end dates."""
        valid_dates = ["2024-01-31", "2022-10-10", "2025-12-25"]
        for date in valid_dates:
            self.assertTrue(validate_date(date))

    def test_end_date_invalid(self):
        """Test invalid end dates."""
        invalid_dates = [
            "2024-02-30",
            "2024-13-01",
            "2024-01-32",
            "invalid-date"
        ]
        for date in invalid_dates:
            self.assertFalse(validate_date(date))

    def test_date_range_valid(self):
        """Test valid date ranges."""
        valid_ranges = [
            ("2024-01-01", "2024-01-31"),
            ("2023-06-01", "2023-06-30"),
            ("2022-10-10", "2022-12-01"),
        ]
        for start_date, end_date in valid_ranges:
            self.assertTrue(validate_date_range(start_date, end_date))

    def test_date_range_invalid(self):
        """Test invalid date ranges."""
        invalid_ranges = [
            ("2024-02-30", "2024-01-01"),
            ("2024-01-01", "2024-13-01"),
            ("2024-01-01", "invalid-date")
        ]
        for start_date, end_date in invalid_ranges:
            self.assertFalse(validate_date_range(start_date, end_date))

if __name__ == "__main__":
    unittest.main()