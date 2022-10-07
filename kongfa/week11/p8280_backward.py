""" _ """


def main():
    """ _ """
    inv = []
    while True:
        invv = input()
        if invv == "NULL":
            break
        else:
            inv.append(invv)
    print("\n".join(inv[::-1]))


main()
