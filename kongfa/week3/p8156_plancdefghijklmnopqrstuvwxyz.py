""" _ """

def main():
    """ _ """
    ascend = input() == "Ascend"
    xxx = float(input())
    yyy = float(input())
    zzz = float(input())
    if xxx > yyy:
        ddd = xxx
        xxx = yyy
        yyy = ddd
    if xxx > zzz:
        ddd = xxx
        xxx = zzz
        zzz = ddd
    if yyy > zzz:
        ddd = yyy
        yyy = zzz
        zzz = ddd

    print('%.2f, %.2f, %.2f' % ((xxx, yyy, zzz) if ascend else (zzz, yyy, xxx)))
main()
