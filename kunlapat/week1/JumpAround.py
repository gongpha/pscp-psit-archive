"""prints transformed user input to console"""


def main() -> int:
    """the main function"""

    var = int(input())

    print(var)
    print(var+5)
    print(var-17)
    print(var*32)
    print(5*var**2+10*5*var+3)

    return 0

if __name__ == "__main__":
    main()
