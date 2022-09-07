"""Prints something to console"""


def main() -> int:
    """The main function"""
    print("_".join([str(x+1) for x in list(range(int(input())))]))

    return 0

if __name__ == "__main__":
    main()
