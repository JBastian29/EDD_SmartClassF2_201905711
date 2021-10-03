class compareTo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a == self.b:
            return 0
        elif self.a > self.b:
            return 1
        elif self.a < self.b:
            return -1
        return 0

