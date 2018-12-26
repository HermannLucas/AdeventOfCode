import unittest
import Code
from datetime import datetime

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.sut = Code.day4()

    def test_read_record(self):

        time_stamp = datetime.strptime("1518-11-01 00:00", '%Y-%m-%d %H:%M')

        problem = "[1518-11-01 00:00] Guard #10 begins shift"
        expected_result = (time_stamp, "Guard #10 begins shift")

        self.assertEqual(next(self.sut.read_records(problem)), expected_result)

    def test_single_record(self):

        problem = "[1518-11-03 00:24] falls asleep"
        expected_result = [24]

        record = next(self.sut.read_records(problem))
        self.sut.add_state_change(record[0])
        self.assertEqual(self.sut.sleep_table["11-03"].changes, expected_result)

    def test_records_of_a_day(self):

        problem = "[1518-11-01 00:00] Guard #10 begins shift, [1518-11-01 00:05] falls asleep, [1518-11-01 00:25] wakes up, [1518-11-01 00:30] falls asleep, [1518-11-01 00:55] wakes up"
        expected_result = {("11-03"): [24]}

        self.sut.problem1(problem)
        self.assertEqual(self.sut.sleep_table, expected_result)


if __name__ == '__main__':
    unittest.main()
