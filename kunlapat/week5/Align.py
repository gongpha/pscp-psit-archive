""" Something Something"""


def main() -> int:
    """Main Function"""
    width = int(input())
    alignment = str(input())
    message = str(input())

    print(
        message.ljust(width) if alignment == "left" else
        message.center(width) if alignment == "center" else
        message.rjust(width)  # if alignment == "right"
    )

    return 0

if __name__ == "__main__":
    main()
