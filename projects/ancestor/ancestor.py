import sys
sys.path.append('./')
from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # initialize graph and a stack
    graph = Graph()
    s = Stack()
    # create a graph with vertices
    for i in range(1, 12):
        graph.add_vertex(i)
    # add paths in ancestors as graph edged
    for pairs in ancestors:
        graph.add_edge(pairs[0], pairs[1])
    # print(graph)
    
    # enqueue the starting node
    s.push(starting_node)
    # print(starting_node, 'starting_node')
    visited = set()
    earliest = -1

    while s.size() > 0:
        v = s.pop()
        print(v, 's.pop()')
        earliest = v
        # print(earliest)

        if v not in visited:
            visited.add(v)
            for next_vertex in graph.vertices[v]:
                print(next_vertex, 'next_vertex')
                s.push(next_vertex)
    print(visited)
    return earliest
