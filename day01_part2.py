
def find_repeated_frequency(numbers):
    total = 0
    previously_seen_frequencies = set([total])
    while True:
        for number in numbers:
            total += number
            if total in previously_seen_frequencies:
                return total
            previously_seen_frequencies.add(total)


input_filename = 'input/day01.txt'
with open(input_filename, 'rt') as input_file:
    numbers = [int(line) for line in input_file if line.strip()]

print(find_repeated_frequency(numbers))
