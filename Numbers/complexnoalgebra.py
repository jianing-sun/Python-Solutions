# Complex number algebra
# good start for programming with class

class number:
    def __init__(self, x, y):
        self.r = x
        self.im = y

    def show(self):
        print(str(self.r) + str('+') + str('i') + str(self.im))

    def negative(self):
        self.r = self.r * (-1)
        self.im = self.im * (-1)
        return self


class compute:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return str((self.n1.r + self.n2.r)) + str('+') + str('i') + str((self.n1.im + self.n2.im))

    def multi(self):
        return str(self.n1.r * self.n2.r - self.n1.im * self.n2.im) + str('+') + str('i') + str(
            self.n1.r * self.n2.im + self.n1.im * self.n2.r)


n1 = number(3, 2)
n2 = number(4, 1)

n1.show()
n2.show()

c = compute(n1, n2)
print(c.multi())
