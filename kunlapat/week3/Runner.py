"""Prints something to console"""


def main() -> int:
    """The main function"""
    print("\n".join([str(input())]*int(input())))

    return 0

if __name__ == "__main__":
    main()
