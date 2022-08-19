"""prints something to console"""


def main() -> int:
    """the main function"""

    num1 = int(input())
    num2 = float(input())
    word = str(input())
    print("{:30d}".format(num1))
    print("{:030d}".format(num1))
    print("{:.2f}".format(num2))
    print("{:.12f}".format(num2))
    print("{:>40s}".format(word))
    return 0

if __name__ == "__main__":
    main()
