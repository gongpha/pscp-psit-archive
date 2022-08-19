"""Prints something to console"""


def main() -> int:
    """The main function"""
    width = int(input())
    height = int(input())

    print(width*height)
    print(width*2+height*2)

    return 0

if __name__ == "__main__":
    main()
