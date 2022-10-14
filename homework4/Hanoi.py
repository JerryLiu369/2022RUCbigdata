LETTERS = ("A", "B", "C")


def hanoi(n, origin: int, mid: int, target: int) -> None:
    if n == 1:
        print(LETTERS[origin] + "->" + LETTERS[target])
        return
    hanoi(n - 1, origin, target, mid)
    print(LETTERS[origin] + "->" + LETTERS[target])
    hanoi(n - 1, mid, origin, target)
    return


hanoi(3, 0, 1, 2)
