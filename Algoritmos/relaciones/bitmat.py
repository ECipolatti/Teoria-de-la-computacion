
class bitmat(object):

    # Se asume matrices cuadradas de 1 y 0 exclusivamente.

    def __init__(self, arg):
        if isinstance(arg, int):
            n = int(arg)
            assert n >= 0
            self.size = n
            self.values = [0] * (n * n)
        elif isinstance(arg, bitmat):
            self.size = arg.size
            self.values = arg.values[:]
        elif isinstance(arg, list):
            n = len(arg)
            self.__init__(n)
            for i in range(n):
                row = arg[i]
                assert len(row) == n
                for j in range(n):
                    self[i, j] = row[j]
        else:
            raise ValueError

    def __eq__(self, other):
        return (self.size   == other.size and
                self.values == other.values)

    def __ne__(self, other):
        return (self.size   != other.size or
                self.values != other.values)

    def __copy__(self):
        return bitmat(self)

    def __repr__(self):
        n = self.size
        rows = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append("%d" % self[i,j])
            rows.append(" ".join(row))
        return "\n".join(rows)

    #

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        n = self.size
        i, j = item
        assert i < n and j < n
        index = i * n + j
        return self.values[index]

    def __setitem__(self, item, value):
        n = self.size
        i, j = item
        assert i < n and j < n
        index = i * n + j
        self.values[index] = int(bool(value))

    #

    def __invert__(self):
        A = self
        n = A.size
        C = bitmat(n)
        for i in range(n):
            for j in range(n):
                C[i,j] = not A[i, j]
        return C

    def __or__(self, other):
        A, B = self, other
        assert A.size == B.size
        n = A.size
        C = bitmat(n)
        for i in range(n):
            for j in range(n):
                C[i,j] = A[i, j] or B[i, j]
        return C

    def __and__(self, other):
        A, B = self, other
        assert A.size == B.size
        n = A.size
        C = bitmat(n)
        for i in range(n):
            for j in range(n):
                C[i,j] = A[i, j] and B[i, j]
        return C

    def __mul__(self, other):
        A, B = self, other
        assert A.size == B.size
        n = A.size
        C = bitmat(n)
        for i in range(n):
            for j in range(n):
                c = False
                for k in range(n):
                    c = c or (A[i, k] and B[k, j])
                C[i,j] = c
        return C
# end
