"""Prints something to console"""


def main() -> int:
    """The main function"""
    print("\n".join([str(x) for x in range(1, 101)]))

    return 0

if __name__ == "__main__":
    main()
