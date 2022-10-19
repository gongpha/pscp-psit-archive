""" _ """


def main():
    """ _ """
    inv = []
    missing = []
    count = int(input())
    while True:
        invv = int(input())
        if invv == 0:
            break
        else:
            inv.append(invv)
    missing = list(range(1, count + 1))
    for iii in inv:
        if iii in missing:
            missing.remove(iii)
    print("\n".join([str(iii) for iii in sorted(missing)]))


main()
