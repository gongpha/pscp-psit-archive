""" Something Something"""


def main() -> int:
    """Main Function"""
    message = "*" + str(input()) + "*"

    print("*"*len(message))
    print(message)
    print("*"*len(message))

    return 0

if __name__ == "__main__":
    main()
