class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = 0
        for item1, item2 in zip(V1, V2):
            result += item1 * item2
        print('check check result -> : ', result)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [item1 + item2 for item1, item2 in zip(V1, V2)]
        print(result)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [item1 - item2 for item1, item2 in zip(V1, V2)]
        print(result)
