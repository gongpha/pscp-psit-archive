"""Print something to the console"""

def main() -> int:
    """The main function (Entry point of the programme)"""
    size = int(input())

    print("{}\n".format(" ".join([str(x) for x in range(1, size+1)]))*size)

    return 0

if __name__ == "__main__":
    main()
