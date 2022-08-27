"""Do something"""
from math import sqrt


def main() -> int:
    """This is the main function"""
    circle_x = float(input())
    circle_y = float(input())
    radius = float(input())
    dot_x = float(input())
    dot_y = float(input())

    print(sqrt((dot_y - circle_y)**2 + (dot_x - circle_x)**2) <= radius)

    return 0


if __name__ == "__main__":
    main()
