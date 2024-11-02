class calculator:

    def __init__(self, vec: list[float]):
        self.vec = vec
    def __add__(self, object) -> None:
        self.vec = [item + object for item in self.vec]
        print(self.vec)
    def __mul__(self, object) -> None:
        self.vec = [item * object for item in self.vec]
        print(self.vec)
    def __sub__(self, object) -> None:
        self.vec = [item - object for item in self.vec]
        print(self.vec)
    def __truediv__(self, object) -> None:
        if (object == 0):
            print("Error: Divide by 0 are not allowed. Are you crazy?")
            return
        self.vec = [item / object for item in self.vec]
        print(self.vec)


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 0