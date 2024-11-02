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
