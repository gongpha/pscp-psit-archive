
"""Prints 'Output' to console"""


def main() -> int:
    """The main function"""
    for i in range(4):
        for _ in range(3):
            print("Output{}".format(i+1))

    return 0

if __name__ == "__main__":
    main()
