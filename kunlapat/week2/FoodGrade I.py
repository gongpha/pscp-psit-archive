"""Print something to the console"""

def main() -> int:
    """The main function"""
    func_1 = lambda weight: int(abs(weight - 60) <= 10)
    func_2 = lambda weight: int(abs(weight - 60) <= 10)
    output = 0

    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))
    output += func_1(int(input()))

    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))
    output += func_2(int(input()))

    print(output)

    return 0


if __name__ == "__main__":
    main()
