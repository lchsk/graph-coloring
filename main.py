from graph.brute_force import BruteForce
from graph.clique_search import CliqueSearch
from graph.graph import Graph

import sys
import getopt

if __name__ == '__main__':

    # Example of 3-colorable graph
    a1 = [0, 1, 2, 1]
    a2 =[1, 2, 3, 4]

    # Example of a graph that is not 3-colorable
    b1 = [0, 1, 2, 3, 0, 1]
    b2 = [1, 2, 3, 0, 2, 3]

    c1 = [0, 1, 2, 3, 2, 2, 4, 5, 1, 0]
    c2 = [1, 2, 3, 0, 4, 5, 5, 6, 3, 2]

    colours_n = 3
    method = 'clique' # 'clique' or 'brute-force'

    opts, args = getopt.getopt(sys.argv[1:], "c:m:", ['colours', 'method'])

    try:
        for opt, arg in opts:
            if opt in ('-c', '--colours'):
                colours_n = int(arg)
            elif opt in ('-m', '--method'):
                method = arg
            else:
                self.help()

    except getopt.GetoptError:
        print 'Error while reading the input'

    g = Graph(list_from=c1, list_to=c2)

    if method == 'brute-force':
        bf = BruteForce(g)
        bf.run(colours_n)
    elif method == 'clique':
        clique = CliqueSearch(g)
        clique.run(colours_n)
