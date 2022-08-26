"""Prints something to console"""


def main() -> int:
    """The main function"""
    if float(input()) < 60:
        print("Fail")
    else:
        print("Pass")
    return 0

if __name__ == "__main__":
    main()
