"""Prints something to console"""


def main() -> int:
    """The main function"""
    print("\n".join([str(input())]*100))

    return 0

if __name__ == "__main__":
    main()
