"""Print something to the console"""

def gen_array(init: list[int], time: int, result=None) -> list[list[int]]:
    """create an list of list with each list got each of its member appended by 1"""
    if result is None:
        result = []

    if time == 0:
        result.append(init)
    else:
        result.append(init)
        gen_array([x+1 for x in init], time - 1, result)
    return result


def main() -> int:
    """The main function (Entry point of the programme)"""
    size = int(input())

    print("\n".join(map(" ".join, [list(map(str, x)) for x in gen_array(list(range(1, size+1)), size)][1:])))

    return 0

if __name__ == "__main__":
    main()
