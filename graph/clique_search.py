class CliqueSearch(object):
    def __init__(self, graph):
        self.graph = graph

    def _get_target_vertices(self, vertex):
        '''Returns a list of vertices that are connected to vertex'''
        target = set()

        for v in xrange(0, len(self.graph.From)):
            if vertex == self.graph.From[v]:
                target.add(self.graph.To[v])
            elif vertex == self.graph.To[v]:
                target.add(self.graph.From[v])

        return list(target)

    def _list_in_list(self, list1, list2):
        '''Returns true if all elements from list1 are present in list2'''

        for i in list1:
            if i not in list2:
                return False

        return True

    def _check_if_clique(self, vertex):
        '''Returns true if vertex is part of a clique'''

        v1 = self._get_target_vertices(vertex)
        v2 = v1 + [vertex]

        # check neighbours as well
        for v in v1:
            # print v, v2, sorted(self._get_target_vertices(v) + [v])
            # if v2 != sorted(self._get_target_vertices(v) + [v]):
            if not self._list_in_list(v2, self._get_target_vertices(v) + [v]):
                return False

        return True

    def run(self, colours_n):

        for v in self.graph.vertices_set:
            if self.graph.count_edges(v) >= colours_n:
                if self._check_if_clique(v):
                    print 'This graph is NOT ' + str(colours_n) + '-colourable.'
                    return

        print 'This graph is ' + str(colours_n) + '-colourable.'
