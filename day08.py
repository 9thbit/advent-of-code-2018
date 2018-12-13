from collections import namedtuple

Node = namedtuple('Node', ['children', 'metadata'])


def read_raw_numbers(filename):
    with open(filename, 'rt') as input_file:
        return list(map(int, input_file.readline().split()))


def read_tree_from_numbers(raw_numbers):
    numbers_iterator = iter(raw_numbers)

    def read_node():
        num_children, num_metadata = next(numbers_iterator), next(numbers_iterator)
        children = [read_node() for child_index in range(num_children)]
        metadata = [next(numbers_iterator) for metadata_index in range(num_metadata)]

        return Node(children, metadata)

    return read_node()


def compute_sum_metadata(node):
    return sum(node.metadata) + sum(compute_sum_metadata(child) for child in node.children)


def compute_child_node_sum(node):
    if not node.children:
        return sum(node.metadata)

    return sum(
        compute_child_node_sum(node.children[child_index - 1])
        for child_index in node.metadata
        if child_index - 1 < len(node.children)
    )


def main():
    # filename = 'input/day08-test.txt'
    filename = 'input/day08.txt'
    raw_numbers = read_raw_numbers(filename)

    root = read_tree_from_numbers(raw_numbers)

    print(compute_sum_metadata(root))  # Part 1
    print(compute_child_node_sum(root))  # Part 2


if __name__ == '__main__':
    main()
