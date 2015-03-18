from graph.brute_force import BruteForce
from graph.graph import Graph

if __name__ == '__main__':

    # Example of 3-colorable graph
    # [0, 1, 2, 1]
    # [1, 2, 3, 4]

    # Example of a graph that is not 3-colorable
    # [0, 1, 2, 3, 0, 1]
    # [1, 2, 3, 0, 2, 3]

    g = Graph(list_from=[0, 1, 2, 3, 0, 1], list_to=[1, 2, 3, 0, 2, 3])
    bf = BruteForce(g)
    bf.check_all_combinations(colours_n=3)
