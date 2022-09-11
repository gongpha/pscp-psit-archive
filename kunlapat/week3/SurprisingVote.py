"""Take some input, does somthing idk"""


def main() -> int:
    """The main function"""
    whole = float(input())
    most = float(input())

    print("Surprising" if (most - (whole - most) / 2) > 2 else "Not surprising")

    return 0

if __name__ == "__main__":
    main()
