input_filename = 'input/day01.txt'
with open(input_filename, 'rt') as input_file:
    print(sum(int(line) if line.strip() else 0 for line in input_file))
