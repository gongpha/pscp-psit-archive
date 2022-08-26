"""Print something to the console"""


def main() -> int:
    """The main function"""
    print([7, 9, 3, 1][(int(input())-1) % 4])

    return 0

if __name__ == "__main__":
    main()
