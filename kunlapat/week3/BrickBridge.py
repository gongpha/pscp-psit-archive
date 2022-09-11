"""Prints something to console"""


def main() -> int:
    """The main function"""
    brick_small = int(input())
    brick_large = int(input())
    goal = int(input())

    use_small = goal % (brick_large * 5)
    use_large = goal // (brick_large * 5)

    if use_large > brick_large:
        pass  # TODO: idk bro just finish this

    if use_small == 0:
        print(-1)
    else:
        if use_small > brick_small:
            print(-1)
        else:
            print(use_small)
    return 0

if __name__ == "__main__":
    main()
