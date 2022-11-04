""" _ """

def main():
    """ _ """
    print([
        kkk[2] - kkk[1] - 1
        if kkk[1] - kkk[0] < kkk[2] - kkk[1] else
        kkk[1] - 1 - kkk[0]
        for kkk in [sorted([int(input()) for _ in range(3)])]
    ][0])

main()
