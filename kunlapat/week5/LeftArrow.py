"""Print left arrow sign of given size"""


def main() -> int:
    """The main function"""
    width = int(input())
    height = int(input())
    gap = int(height/2)

    hit_zero = False

    for _ in range(height):
        print(" "*gap + "*"*width, sep="")
        if gap <= 0:
            hit_zero = True
        gap += 1 if hit_zero else -1

    return 0


if __name__ == "__main__":
    main()
