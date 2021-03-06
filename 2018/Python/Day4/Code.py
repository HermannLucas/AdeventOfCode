import re
import datetime
from operator import itemgetter

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

    def __init__(self):
        self.sleep_table = {}
        self.guard_state_changes = {}

    def read_records(self, records):
        for record in records.split(", "):
            match = re.match(r'\[(.*)\] (.*)', record)
            yield self.read_time_stamp(match.group(1)), match.group(2)

    def read_time_stamp(self, time_stamp):
        return datetime.datetime.strptime(time_stamp, '%Y-%m-%d %H:%M')

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
        if time_stamp.strftime('%H') == "23":
            time_stamp += datetime.timedelta(days=1)
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

    def find_sleeper(self):
        sleep_time = {}
        for day in self.sleep_table.values():
            try:
                sleep_time[day.guard_id] += sum([sleep[1] - sleep[0] for sleep \
                    in (zip(day.changes[::2], day.changes[1::2]))])
            except:
                sleep_time[day.guard_id] = sum([sleep[1] - sleep[0] for sleep \
                    in (zip(day.changes[::2], day.changes[1::2]))])
        return max(sleep_time, key= sleep_time.get)

    def find_most_asleep(self, guard_id):
        rec = {}
        tot = 0
        count = 1
        state_changes = {}
        for day in self.sleep_table.values():
            if guard_id == day.guard_id:
                for change in day.changes:
                    try:
                        state_changes[change] += count
                    except:
                        state_changes[change] = count
                    count *= -1
        self.guard_state_changes[guard_id] = state_changes
        for guard_id, change in sorted(state_changes.items()):
            tot += change
            rec[guard_id] = tot
        try:
            return max(rec, key = rec.get)
        except:
            return None

    def problem1(self, records):
        self.fill_sleep_table(records)
        guard_id = self.find_sleeper()
        minute = self.find_most_asleep(guard_id)
        return guard_id * minute

    def problem2(self, records):
        self.fill_sleep_table(records)
        guards = {day.guard_id: () for day in self.sleep_table.values()}
        for guard in guards.keys():
            minute = self.find_most_asleep(guard)
            try:
                guards[guard] = (minute, self.guard_state_changes[guard][minute])
            except:
                guards[guard] = None
        print(guards)
