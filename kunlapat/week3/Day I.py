"""Prints something to console"""


def main() -> int:
    """The main function"""
    year = int(input())

    if year % 4 != 0:
        print("No")
    elif year % 100 != 0:
        print("Yes")
    elif year % 400 != 0:
        print("No")
    else:
        print("Yes")

    return 0

if __name__ == "__main__":
    main()
