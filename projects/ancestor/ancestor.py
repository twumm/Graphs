import sys
sys.path.append('./')
from graph import Graph
from util import Stack, Queue

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    # initialize graph and build it
    graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    # create a queue and enqueue the starting node
    q = Queue()
    q.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        # current_node is last in the path
        current_node = path[-1]

        if (len(path) >= longest_path_length and current_node < earliest_ancestor) or len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        # if len(path) > longest_path_length:
        #     longest_path_length = len(path)
        #     earliest_ancestor = current_node
        print(current_node)
        neighbours = graph.vertices[current_node]
        for ancestor in neighbours:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)
    # print(path)
    # print(earliest_ancestor)
    return earliest_ancestor
