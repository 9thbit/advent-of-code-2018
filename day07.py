from collections import defaultdict
import re


def read_input(filename):
    step_re = re.compile('Step (?P<from_step>\w+) must be finished before step (?P<to_step>\w+) ')
    with open(filename, 'rt') as input_file:
        for line in input_file:
            match = step_re.search(line)
            if match:
                group_dict = match.groupdict()
                yield group_dict['from_step'], group_dict['to_step']


def build_graph(edge_list):
    # Graphs are represented by an adjacency list of directed edges
    graph = defaultdict(set)
    # reversed_graph = defaultdict(set)

    for from_node, to_node in edge_list:
        if from_node not in graph:
            graph[from_node] = set()  # Force all nodes to have nodes in the graph

        graph[to_node].add(from_node)
        # reversed_graph[from_node].add(to_node)

    return graph


def build_lexicographic_topologically_sorted_nodes(graph):
    topological_sorted_nodes = []
    while graph:
        sorted_zero_degree_nodes = sorted([
            node for node, incoming_edges in graph.items() if not incoming_edges
        ])

        if not sorted_zero_degree_nodes:
            raise Exception('Cycle detected, topological sort is undefined.')

        first_zero_degree_node = sorted_zero_degree_nodes[0]
        topological_sorted_nodes.append(first_zero_degree_node)

        graph = {
            node: incoming_edges - {first_zero_degree_node}
            for node, incoming_edges in graph.items()
            if node != first_zero_degree_node
        }

    return topological_sorted_nodes


def main():
    # filename = 'input/day07-test.txt'
    filename = 'input/day07.txt'
    edge_list = read_input(filename)

    graph = build_graph(edge_list)

    topological_sorted_nodes = build_lexicographic_topologically_sorted_nodes(graph)
    print(''.join(topological_sorted_nodes))


if __name__ == '__main__':
    main()
