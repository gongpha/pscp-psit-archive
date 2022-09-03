""" _ """
def main():
    """ _ """
    aaa = int(input())
    bbb = int(input())
    print("\n".join([str(x) for x in list(
        range(aaa, bbb + 1) if aaa < bbb else range(aaa, bbb - 1, -1)
    )]))
main()
