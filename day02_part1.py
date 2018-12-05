from collections import Counter

two_count, three_count = 0, 0
input_filename = 'input/day02.txt'
with open(input_filename, 'rt') as input_file:
    for line in input_file:
        character_count = Counter(line)
        occurrences_count = Counter(character_count.values())
        two_count += bool(occurrences_count[2])
        three_count += bool(occurrences_count[3])

print(two_count * three_count)
