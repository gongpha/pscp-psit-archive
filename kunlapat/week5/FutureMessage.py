""" Something Something"""


def main() -> int:
    """Main Function"""
    message = str(input())

    print(
        "Number" if message.isdigit() else
        "Uppercase" if message.isupper() else
        "Lowercase" if message.islower() else
        "Title" if message.istitle() else
        "Space" if message.isspace() else
        "Other"
    )

    return 0

if __name__ == "__main__":
    main()
