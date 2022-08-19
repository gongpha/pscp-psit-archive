"""Prints 'Output' to console"""


def main() -> int:
    """The main function"""
    wagon = input() + input()
    length = int(input())

    print(wagon, sep="")
    print(wagon*length, sep="")

    return 0

if __name__ == "__main__":
    main()
