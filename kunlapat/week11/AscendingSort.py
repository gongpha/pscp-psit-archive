"""erhsjotirfgdnk"""


def print_sort(array) -> str:
    """The argument must be of type Iterable[int].
    (I can't do argument type hinting because the python on
    the server is either outdated or I am really just too stupid.)"""
    return "\n".join(map(str, sorted(array)))

if __name__ == "__main__":
    print(print_sort([int(input()), int(input()), int(input()), int(input()), int(input())]))
    