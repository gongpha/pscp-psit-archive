"""Prints something to console"""


def main() -> int:
    """The main function"""
    print("{:.1f} Celsius".format((float(input())-32)/1.8))

    return 0

if __name__ == "__main__":
    main()
