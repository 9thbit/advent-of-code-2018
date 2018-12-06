from collections import defaultdict
from datetime import datetime, timedelta
import re


SLEEP_STRING = 'falls asleep'
WAKE_STRING = 'wakes up'


class Guard:

    def __init__(self):
        self.sleep_minutes = timedelta()
        self.last_sleep_start_time = None
        self.minutes_asleep_by_minute = defaultdict(timedelta)

    def fall_asleep(self, timestamp):
        self.last_sleep_start_time = timestamp

    def wake_up(self, wake_up_timestamp):
        one_minute = timedelta(minutes=1)

        asleep_timestamp = self.last_sleep_start_time
        while asleep_timestamp < wake_up_timestamp:
            self.minutes_asleep_by_minute[asleep_timestamp.minute] += one_minute
            asleep_timestamp += one_minute
            self.sleep_minutes += one_minute

    def get_laziest_minute(self):
        times_asleep, minute = max(
            (times_asleep, minute)
            for minute, times_asleep in self.minutes_asleep_by_minute.items()
        )
        return minute


def read_input(filename):
    log_re = re.compile(
        '\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)] '
        f'((?P<sleep_command>{SLEEP_STRING}|{WAKE_STRING})|Guard #(?P<guard_id>\d+) begins shift)'
    )
    with open(filename, 'rt') as input_file:
        for line in input_file:
            match = log_re.search(line)
            if match:
                groupdict = match.groupdict()

                timestamp = datetime(
                    year=int(groupdict['year']),
                    month=int(groupdict['month']),
                    day=int(groupdict['day']),
                    hour=int(groupdict['hour']),
                    minute=int(groupdict['minute']),
                )
                sleep_command = groupdict['sleep_command']
                guard_id = int(groupdict['guard_id']) if groupdict['guard_id'] else None

                yield timestamp, sleep_command, guard_id


def build_guard_sleep_totals(guard_log):
    guard_map = defaultdict(Guard)
    last_guard_id = None
    for timestamp, sleep_command, guard_id in guard_log:
        last_guard_id = guard_id or last_guard_id
        guard = guard_map[last_guard_id]

        if sleep_command == SLEEP_STRING:
            guard.fall_asleep(timestamp)
        elif sleep_command == WAKE_STRING:
            guard.wake_up(timestamp)

    return guard_map


def get_laziest_guard(guard_map):
    sleep_minutes, laziest_guard, laziest_guard_id = max(
        (guard.sleep_minutes, guard, guard_id)
        for guard_id, guard in guard_map.items()
    )
    return laziest_guard, laziest_guard_id


def get_most_commonly_asleep_guard(guard_map):
    (times_asleep, minute), guard_id = max(
        (
            max(
                (times_asleep, minute)
                for minute, times_asleep in guard.minutes_asleep_by_minute.items()
            ),
            guard_id
        )
        for guard_id, guard in guard_map.items()
        if guard.minutes_asleep_by_minute
    )
    return guard_id, minute


def main():
    filename = 'input/day04.txt'
    guard_log = read_input(filename)
    guard_map = build_guard_sleep_totals(guard_log)

    laziest_guard, laziest_guard_id = get_laziest_guard(guard_map)
    laziest_minute = laziest_guard.get_laziest_minute()

    print(laziest_guard_id * laziest_minute)

    guard_id, minute = get_most_commonly_asleep_guard(guard_map)
    print(guard_id * minute)


if __name__ == '__main__':
    main()
