
"""Do something"""
from math import sqrt


def main() -> int:
    """This is the main function"""
    circle1_x = float(input())
    circle1_y = float(input())
    radius1 = float(input())
    circle2_x = float(input())
    circle2_y = float(input())
    radius2 = float(input())

    if sqrt((circle1_y - circle2_y)**2 + (circle1_x - circle2_x)**2) < radius1 + radius2:
        print("Yes")
    else:
        print("No")

    return 0


if __name__ == "__main__":
    main()
