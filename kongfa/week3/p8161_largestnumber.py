""" _ """

def cmp(aaa, bbb):
    """
        dear Gun, I supposed to use lambda.
        but bruh pylint doesn't like my choice.
    """
    return str(aaa) + str(bbb) > str(bbb) + str(aaa)

def main():
    """ _ """
    xxx = abs(int(input()))
    yyy = abs(int(input()))
    zzz = abs(int(input()))
    if cmp(xxx, yyy):
        ddd = xxx
        xxx = yyy
        yyy = ddd
    if cmp(xxx, zzz):
        ddd = xxx
        xxx = zzz
        zzz = ddd
    if cmp(yyy, zzz):
        ddd = yyy
        yyy = zzz
        zzz = ddd

    print(int(str(zzz) + str(yyy) + str(xxx)))
main()
