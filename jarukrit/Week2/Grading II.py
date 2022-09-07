"""Converts seconds into a timestamp"""


def main() -> int:
    """The main function"""
    score = float(input())
    if score > 100 or score < 0:
        print("ERR")
    elif score < 60:
        print("F")
    elif score < 65:
        print("F+")
    elif score < 70:
        print("D")
    elif score < 75:
        print("D+")
    elif score < 80:
        print("C")
    elif score < 85:
        print("C+")
    elif score < 90:
        print("B")
    elif score < 95:
        print("B+")
    elif score <= 100:
        print("A")

    return 0

if __name__ == "__main__":
    main()
