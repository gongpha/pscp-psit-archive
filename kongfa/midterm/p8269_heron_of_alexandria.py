""" _ """
def main():
    """ _ """
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    sss = (aaa + bbb + ccc) / 2
    print("%.3f" % (sss * (sss - aaa) * (sss - bbb) * (sss - ccc)) ** 0.5)
main()
