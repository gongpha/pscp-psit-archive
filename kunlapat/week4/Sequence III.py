"""Print something to the console"""

def main() -> int:
    """The main function (Entry point of the programme)"""
    size = int(input())

    # I give up
    for y in range(size):
        for x in range(size):
            print(x+y+2, end=" ")
        print() # newline

    return 0

if __name__ == "__main__":
    main()
