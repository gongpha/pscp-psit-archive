"""Converts seconds into a timestamp"""


def main() -> int:
    """The main function"""
    point_q1, point_q2 = float(input()), float(input())
    point_p1, point_p2 = float(input()), float(input())
    point_q, point_p = (point_q1 - point_p1)**2, (point_q2 - point_p2)**2
    print((point_q + point_p)**(1/2))
    return 0

if __name__ == "__main__":
    main()
