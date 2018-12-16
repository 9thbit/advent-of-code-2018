from collections import defaultdict


def calculate_power_level(grid_serial_number, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5
    return power_level


def build_power_level_map(grid_serial_number, max_x, max_y):
    power_level_map = defaultdict(int)
    for x in range(1, max_x + 1):
        for y in range(1, max_y + 1):
            power_level_map[(x, y)] = calculate_power_level(grid_serial_number, x, y)

    return power_level_map


def build_cumulative_sum_map(power_level_map, max_x, max_y):
    cumulative_sum_map = defaultdict(int)
    for x in range(1, max_x + 1):
        for y in range(1, max_y + 1):
            cumulative_sum_map[(x, y)] = sum((
                power_level_map[(x, y)],
                cumulative_sum_map[(x - 1, y)],
                cumulative_sum_map[(x, y - 1)],
                -cumulative_sum_map[(x - 1, y - 1)],
            ))

    return cumulative_sum_map


def find_largest_sum(cumulative_sum_map, max_x, max_y, width=3, height=3):
    largest_sum, (bottom_right_x, bottom_right_y) = max(
        (
            sum((
                cumulative_sum_map[(x, y)],
                -cumulative_sum_map[(x - width, y)],
                -cumulative_sum_map[(x, y - height)],
                cumulative_sum_map[(x - width, y - height)],
            )),
            (x, y)
        )
        for x in range(width, max_x + 1)
        for y in range(height, max_y + 1)
    )
    return largest_sum, bottom_right_x - width + 1, bottom_right_y - height + 1


def find_largest_sum_of_any_size(cumulative_sum_map, max_x, max_y, max_size):
    (largest_sum, x, y), size_of_largest_sum = max(
        (
            find_largest_sum(cumulative_sum_map, max_x, max_y, width=size, height=size),
            size,
        )
        for size in range(1, max_size + 1)
    )
    return x, y, size_of_largest_sum



def main():
    grid_serial_number = 7315
    max_size = 300

    power_level_map = build_power_level_map(grid_serial_number, max_x=max_size, max_y=max_size)
    cumulative_sum_map = build_cumulative_sum_map(power_level_map, max_x=max_size, max_y=max_size)
    _, x, y = find_largest_sum(cumulative_sum_map, max_x=max_size, max_y=max_size)
    print(f'{x},{y}')  # Part 1

    x, y, size_of_largest_sum = find_largest_sum_of_any_size(
        cumulative_sum_map,
        max_x=max_size,
        max_y=max_size,
        max_size=max_size,
    )
    print(f'{x},{y},{size_of_largest_sum} ')  # Part 2


if __name__ == "__main__":
    main()
