import re


class Point:

    def __init__(self, x, y, vx, vy):
        self.original_x = self.x = x
        self.original_y = self.y = y
        self.vx, self.vy = vx, vy

    def simulate_steps(self, num_steps=1):
        self.x = self.original_x + self.vx * num_steps
        self.y = self.original_y + self.vy * num_steps


def read_input(filename):
    point_re = re.compile(
        'position=<[ ]*(?P<x>[-]?\d+),[ ]*(?P<y>[-]?\d+)> '
        'velocity=<[ ]*(?P<vx>[-]?\d+),[ ]*(?P<vy>[-]?\d+)>'
    )
    points = []
    with open(filename, 'rt') as input_file:
        for line in input_file:
            match = point_re.search(line)
            if match:
                group_dict = match.groupdict()
                points.append(
                    Point(
                        x=int(group_dict['x']),
                        y=int(group_dict['y']),
                        vx=int(group_dict['vx']),
                        vy=int(group_dict['vy']),
                    )
                )
    return points


def get_bounding_box(points):
    min_x = min(point.x for point in points)
    min_y = min(point.y for point in points)
    max_x = max(point.x for point in points)
    max_y = max(point.y for point in points)
    return min_x, min_y, max_x, max_y


def get_bounding_area_for_step_count(points, step_count):
    for point in points:
        point.simulate_steps(num_steps=step_count)

    min_x, min_y, max_x, max_y = get_bounding_box(points)
    return (max_x - min_x) * (max_y - min_y)


def print_grid(points):
    min_x, min_y, max_x, max_y = get_bounding_box(points)

    width = (max_x - min_x) + 1
    height = (max_y - min_y) + 1

    grid = [[' '] * width for y in range(height)]
    for point in points:
        grid[point.y - min_y][point.x - min_x] = '#'

    for row in grid:
        print(''.join(row))


def main():
    # filename = 'input/day10-test.txt'
    filename = 'input/day10.txt'
    points = read_input(filename)

    # First expentially increase the step counts to quickly find an upper bound on step count
    step_count = 0
    step_increment = 1
    steps_lower_bound, steps_upper_bound = step_count, None
    last_area_size = get_bounding_area_for_step_count(points, step_count)

    while True:
        step_count += step_increment
        area_size = get_bounding_area_for_step_count(points, step_count)

        if area_size > last_area_size:
            steps_upper_bound = step_count
            steps_lower_bound = step_count - step_increment
            break

        last_area_size = area_size
        step_increment *= 2

    # At this point, ideally we would do binary search between the lower and upper bounds, but the
    # area is not guaranteed to be monotonically increasing, and a linear search is sufficient.
    minimum_area, minimum_step_count = min(
        (get_bounding_area_for_step_count(points, step_count), step_count)
        for step_count in range(steps_lower_bound, steps_upper_bound + 1)
    )

    # Draw the message
    for point in points:
        point.simulate_steps(num_steps=minimum_step_count)
    print_grid(points)

    print("Part2:", minimum_step_count)


if __name__ == '__main__':
    main()
