class BruteForce(object):

    def __init__(self, graph):
        self.graph = graph

    def representation(self, n, base):
        '''Changes number n to a base-b representation'''

        result = []

        while True:
            d = n / base
            m = n % base

            if not d and not m:
                break

            result.append(m)

            n = d

        return result

    def fix(self, r, length):

        # Fill with zeroes at the beginning
        while len(r) < length:
            r.append(0)

        # Inverse the lsit
        return r[::-1]

    def check(self, colour):

        for i in xrange(0, self.graph.E):
            v1 = self.graph.From[i]
            v2 = self.graph.To[i]

            # Check if vertices are of the same colour
            if colour[v1] == colour[v2]:
                # print 'Error : same colour for vertices %d and %d' % (col1, col2)
                return False

        return True

    def run(self, colours_n):

        # Number of combinations is colours^vertices
        for i in xrange(0, colours_n**self.graph.V):

            colour = self.fix(self.representation(i, colours_n), self.graph.V)
            print colour

            if self.check(colour):
                print 'Graph is ' + str(colours_n) + '-colourable. Colours: ' + str(colour)
                return

        print 'Graph is NOT ' + str(colours_n) + '-colourable.'
