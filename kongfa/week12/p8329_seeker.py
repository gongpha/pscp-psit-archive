""" _ """
def main():
    """ _ """
    bbb = ""
    vvv = 0
    for ccc in input():
        if ccc.isdigit():
            bbb += ccc
        else:
            vvv += int(bbb) if len(bbb) > 0 else 0
            bbb = ""
    print(vvv + (int(bbb) if bbb.isdigit() else 0))
main()
