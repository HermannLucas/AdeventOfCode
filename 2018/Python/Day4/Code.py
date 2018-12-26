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

    def read_records(self, records):
        for record in records.split(", "):
            match = re.match(r'\[(.*)\] (.*)', record)
            yield self.read_time_stamp(match.group(1)), match.group(2)

    def read_time_stamp(self, time_stamp):
        return datetime.strptime(time_stamp, '%Y-%m-%d %H:%M')

    def read_guard_id(self, text):
        return int(re.match(r'Guard #(.*) begins shift', text).group(1))

    def add_state_change(self, time_stamp):
        try:
            self.sleep_table[time_stamp.strftime('%m-%d')]\
                .changes.append(int(time_stamp.strftime('%M')))
        except:
            self.sleep_table[time_stamp.strftime("%m-%d")] = \
                Record.with_change(int(time_stamp.strftime('%M')))

    def add_guard_id(self, time_stamp, guard_id):
        try:
            self.sleep_table[time_stamp.strftime('%m-%d')]\
                .guard_id = guard_id
        except:
            self.sleep_table[time_stamp.strftime('%m-%d')] = \
                Record.with_id(guard_id)

    def fill_sleep_table(self, records):
        for time_stamp, text in self.read_records(records):
            if "Guard" in text:
                self.add_guard_id(time_stamp, self.read_guard_id(text))
            else:
                self.add_state_change(time_stamp)

        for day in self.sleep_table.values():
            day.changes.sort()
