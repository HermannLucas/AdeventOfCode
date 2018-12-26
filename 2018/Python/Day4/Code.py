import re
from datetime import datetime

class Record(object):

    def __init__(self, guard_id, changes):
        self.guard_id = guard_id
        self.changes = changes

    @classmethod
    def with_id(cls, guard_id):
        return cls(guard_id, [])

    @classmethod
    def with_change(cls, change):
        return cls("", [change])

class day4(object):
    sleep_table = {}

    def read_record(self, record):
        match = re.match(r'\[(.*)\] (.*)', record)
        return self.read_time_stamp(match.group(1)), match.group(2)

    def read_time_stamp(self, time_stamp):
        return datetime.strptime(time_stamp, '%Y-%m-%d %H:%M')

    def add_record(self, record):
        time_stamp, text = self.read_record(record)
        try:
            self.sleep_table[time_stamp.strftime('%m-%d')]\
                .changes.append(int(time_stamp.strftime('%M')))
            print("Fails")
        except:
            self.sleep_table[time_stamp.strftime("%m-%d")] = \
                Record.with_change(int(time_stamp.strftime('%M')))

    def problem1(self, records):
        pass
