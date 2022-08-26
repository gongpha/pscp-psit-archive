"""Prints something to console"""


def main() -> int:
    """The main function"""
    name, age = input(), float(input())
    if age < 18:
        print("{0}, you can pass.".format(name))
    else:
        print("{0}, you shall not pass.".format(name))

if __name__ == "__main__":
    main()
