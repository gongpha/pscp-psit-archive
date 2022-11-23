""" _ """
def main():
    """ _ """
    nnn1 = int(input())
    nnn2 = int(input())
    while nnn2:
        nnn1, nnn2 = nnn2, nnn1 % nnn2
    print(
        "YES\n%d" % nnn1 if nnn1 == 1 else "NO\n%d" % nnn1
    )
main()
