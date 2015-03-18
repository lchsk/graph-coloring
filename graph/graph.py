
class Graph(object):
    def __init__(self, list_from, list_to):

        self.tmp = set()

        for i in list_from + list_to:
            self.tmp.add(i)

        self.V = len(self.tmp)

        #self.V = vertices
        self.E = len(list_from)

        self.From = [0] * self.E
        self.To = [0] * self.E

        self.From = list_from
        self.To = list_to
