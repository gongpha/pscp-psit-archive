""" _ """
def main():
    """ _ """
    ccc = int(input())
    mmm = sorted([int(input()) for _ in range(ccc)])
    hhh = sorted([int(input()) for _ in range(ccc)])
    print(max((abs(int(mmm[i]) - int(hhh[i]))) for i in range(ccc)))
main()
