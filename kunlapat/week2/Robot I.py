"""Converts seconds into a timestamp"""


def main() -> int:
    """The main function"""
    name = str(input())
    age = float(input())

    if age < 18:
        print("{}, you can pass.".format(name))
    else:
        print("{}, you shall not pass.".format(name))


    return 0

if __name__ == "__main__":
    main()
