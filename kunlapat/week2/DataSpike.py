"""Print something to the console"""


def main() -> int:
    """The main function"""
    output = int(input())

    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data
    data = int(input())
    if data > output:
        output = data

    print(output)

    return 0


if __name__ == "__main__":
    main()
