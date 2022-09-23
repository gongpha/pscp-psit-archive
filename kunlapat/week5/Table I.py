"""This Programme does somthing"""

def main() -> int:
    """This is the main function"""
    for index in map(lambda x: x+1, range(int(input()))):
        print("15 x {} = {}".format(index, index*15))

    return 0

if __name__ == "__main__":
    main()
