"""Print something to the console"""


def main() -> int:
    """The main function"""
    output = 0

    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift
    gift = int(input())
    if gift % 2 == 0:
        output = gift

    print(output)

    return 0


if __name__ == "__main__":
    main()
