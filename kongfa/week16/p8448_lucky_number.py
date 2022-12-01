""" _ """
def main():
    """ _ """
    lll = list(range(1, int(input()) + 1, 2))
    iii = 1
    while iii < len(lll):
        del lll[lll[iii] - 1::lll[iii]]
        iii += 1
    print(*lll)
main()
