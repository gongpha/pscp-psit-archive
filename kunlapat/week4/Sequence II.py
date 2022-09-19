"""Print something to the console"""

def main() -> int:
    """The main function (Entry point of the programme)"""
    size = int(input())

    print(" ".join([str(x) for x in [x**2 for x in range(1, size+1)]]))

    return 0

if __name__ == "__main__":
    main()
