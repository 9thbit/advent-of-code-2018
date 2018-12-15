from collections import defaultdict
from itertools import cycle
import re

from blist import blist  # more efficient insert and deletion than built in list


class MarbleCircle:

    def __init__(self):
        self.circle = blist([0])
        self.current_index = 0

    def place_marble_and_compute_score(self, marble_number):
        if marble_number % 23 == 0:
            self.current_index = (self.current_index - 7 + len(self.circle)) % len(self.circle)
            return self.circle.pop(self.current_index) + marble_number

        self.current_index = (self.current_index + 2) % len(self.circle)
        self.circle.insert(self.current_index, marble_number)
        return 0


def read_input(filename):
    param_re = re.compile('(?P<num_elves>\d+) players; last marble is worth (?P<last_marble>\d+)')
    with open(filename, 'rt') as input_file:
        for line in input_file:
            match = param_re.search(line)
            if match:
                groupdict = match.groupdict()
                yield int(groupdict['num_elves']), int(groupdict['last_marble'])


def simulate_game(num_elves, last_marble):
    circle = MarbleCircle()
    elve_scores = defaultdict(int)
    elves = cycle(range(num_elves))

    for marble_number in range(1, last_marble + 1):
        elve_scores[next(elves)] += circle.place_marble_and_compute_score(marble_number)

    return max(elve_scores.values())


def main():
    # filename = 'input/day09-test.txt'
    filename = 'input/day09.txt'
    game_parameters = read_input(filename)

    for num_elves, last_marble in game_parameters:
        print(simulate_game(num_elves, last_marble))  # Part 1
        print(simulate_game(num_elves, last_marble * 100))  # Part 2


if __name__ == '__main__':
    main()
