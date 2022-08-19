"""Generates a burger"""


def main() -> int:
    """The main function"""
    top_bun = int(input())
    bottom_bun = int(input())

    print("|"*top_bun+"*"*(2*(top_bun+bottom_bun))+"|"*bottom_bun)

    return 0

if __name__ == "__main__":
    main()
