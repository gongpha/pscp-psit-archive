"""Prints something to console"""


def main() -> int:
    """The main function"""
    # print("\n".join([str(x) for x in list(range(int(input()), int(input())+1))]))

    mmm = int(input())
    nnn = int(input())
    ccc = abs(mmm - nnn) + 1

    for _ in range(ccc):
        print(mmm)
        mmm += (-1 if mmm > nnn else 1)

    return 0

if __name__ == "__main__":
    main()
