from itertools import combinations

input_filename = 'input/day02.txt'
with open(input_filename, 'rt') as input_file:
    words = [line.strip() for line in input_file if line.strip()]

for string1, string2 in combinations(words, 2):
    common_substring = "".join(
        char1 for char1, char2 in zip(string1, string2) if char1 == char2
    )
    if len(common_substring) == len(string1) - 1:
        print(common_substring)
        break
