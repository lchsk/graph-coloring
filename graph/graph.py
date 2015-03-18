
class Graph(object):
    def __init__(self, list_from, list_to):

        # All vertices
        self.vertices_set = set()
        for i in list_from + list_to:
            self.vertices_set.add(i)

        # Number of vertices
        self.V = len(self.vertices_set)

        # Number of edges
        self.E = len(list_from)

        # Definition of the graph
        # ith edge points from vertex From[i] to vertex To[i]
        self.From = list_from
        self.To = list_to

    def count_edges(self, vertex):
        '''Returns number of edges that are connected to a vertex'''

        edges = 0

        for v in self.From + self.To:
            if v == vertex:
                edges += 1

        return edges
