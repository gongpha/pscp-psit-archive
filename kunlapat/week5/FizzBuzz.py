"""This Programme does somthing"""

def fizz_buzz(arg: int):
    """Do FizzBuzz on a index"""
    if arg%15 == 0:
        return "FizzBuzz"
    elif arg%3 == 0:
        return "Fizz"
    elif arg%5 == 0:
        return "Buzz"
    else:
        return arg


def main() -> int:
    """This is the main function"""
    length = int(input())

    print("\n".join([*map(str, map(fizz_buzz, map(lambda x: x+1, range(length))))]))

    return 0

if __name__ == "__main__":
    main()
