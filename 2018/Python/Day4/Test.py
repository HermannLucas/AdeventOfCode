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

    def test_single_record_state_change(self):

        problem = "[1518-11-03 00:24] falls asleep"
        expected_result = [24]

        record = next(self.sut.read_records(problem))
        self.sut.add_state_change(record[0])
        self.assertEqual(self.sut.sleep_table["11-03"].changes, expected_result)

    def test_single_record_guard_id(self):

        problem = "[1518-11-01 00:00] Guard #10 begins shift"
        expected_result = 10

        time_stamp, text = next(self.sut.read_records(problem))
        self.sut.add_guard_id(time_stamp, self.sut.read_guard_id(text))
        self.assertEqual(self.sut.sleep_table["11-01"].guard_id, expected_result)

    def test_records_of_a_day(self):

        problem = "[1518-11-01 00:00] Guard #10 begins shift, [1518-11-01 00:05] falls asleep, [1518-11-01 00:25] wakes up, [1518-11-01 00:30] falls asleep, [1518-11-01 00:55] wakes up"
        expected_result_keys = ["11-01"]
        expected_result_changes = [5, 25, 30, 55]

        self.sut.fill_sleep_table(problem)
        self.assertEqual([*self.sut.sleep_table], expected_result_keys)
        self.assertEqual(self.sut.sleep_table["11-01"].changes, expected_result_changes)


if __name__ == '__main__':
    unittest.main()
