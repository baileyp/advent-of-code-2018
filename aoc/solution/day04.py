import re
from collections import defaultdict
from datetime import datetime

WAKE = 'wakes up'
SLEEPS = 'falls asleep'
SHIFT = 'begins shift'

def part1(file):
    """
    O(n log n + g) time complexity, and O(n + g) space complexity, where g is the number of guards in the input.
    :param file:
    :return:
    """
    guards = build_sleep_map(file)

    slept_most = (0, 0)
    for guard, minutes_asleep in guards.items():
        minutes_slept = sum(minutes_asleep.values())
        if minutes_slept > slept_most[1]:
            slept_most = (guard, minutes_slept)

    most_slept_minute = (0, 0)
    for minute, times in guards[slept_most[0]].items():
        if times > most_slept_minute[1]:
            most_slept_minute = (minute, times)

    return slept_most[0] * most_slept_minute[0]

def part2(file):
    """
    O(n log n + g) time complexity, and O(n + g) space complexity, where g is the number of guards in the input.
    :param file:
    :return:
    """
    guards = build_sleep_map(file)

    maxim = (0, 0, 0)
    for guard, minutes_asleep in guards.items():
        for minute, times in minutes_asleep.items():
            if times > maxim[2]:
                maxim = (guard, minute, times)

    return maxim[0] * maxim[1]

def build_sleep_map(notes):
    """
    Builds deep map of guard id => minute slept => number of times asleep at minute
    :param notes:
    :return:
    """
    notes = list(map(parse_note, notes))
    notes.sort(key=lambda t: t[2])

    guards = defaultdict(lambda: defaultdict(lambda: 0))
    guard_on_duty = None
    asleep_at = None
    for who, what, when in notes:
        guard_on_duty = who or guard_on_duty
        if what == SLEEPS:
            asleep_at = when
        if what == WAKE:
            for minute in range(int((when - asleep_at).total_seconds() / 60)):
                guards[guard_on_duty][asleep_at.minute + minute] += 1

    return guards


def parse_note(note):
    pattern = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})] (.*)$")
    guard_id = None
    if pattern.match(note):
        date, action = pattern.findall(note).pop()
        if action not in (WAKE, SLEEPS):
            guard_id = int(re.findall(r"\d+", action).pop())
            action = SHIFT
        return guard_id, action, datetime.strptime(date, '%Y-%m-%d %H:%M')
    raise ValueError("Invalid note format")
