""" _ """

def main():
    """ _ """
    nnn = int(input())
    count = nnn * 2 - 1
    for yyy in range(1, count + 1):
        aaa = nnn - (yyy - 1) if yyy <= nnn else yyy - nnn + 1
        sub = False
        for xxx in range(1, count + 1):
            print('%02d' % aaa, end=' ')
            sub = True if aaa == nnn else False if aaa == (
                yyy if yyy <= nnn else nnn + nnn - yyy
            ) and xxx <= nnn else sub
            aaa += -1 if sub else 1
        print()
main()
