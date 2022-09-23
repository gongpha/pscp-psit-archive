
"""Prints something to console"""


def main() -> int:
    """The main function"""
    side_a = float(input())
    side_b = float(input())
    side_c = float(input())

    print("Yes" if abs(side_a**2 - (side_b**2 + side_c**2)) <= 0.01
          or abs(side_c**2 - (side_b**2 + side_a**2)) <= 0.01
          or abs(side_b**2 - (side_a**2 + side_c**2)) <= 0.01
          else "No")

    return 0

if __name__ == "__main__":
    main()
