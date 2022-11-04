""" _ """

from math import floor, ceil


def main():
    """ _ """
    ppp = float(input()), float(input())
    qqq = float(input()), float(input())

    def ccc(ppp):
        """ _ """
        xxx, yyy = ppp
        if isinstance(xxx, float):
            return [(floor(xxx), yyy), (ceil(xxx), yyy)]
        else:
            return [(xxx, floor(yyy)), (xxx, ceil(yyy))]
    def ttt(ppp, qqq):
        """ _ """
        xxx, yyy = ppp
        zzz, www = qqq
        return abs(xxx - zzz) + abs(yyy - www)
    print('%.2f' % (
        min(ttt(ppp, c) + ttt(c, d) + ttt(d, qqq)
            for c in ccc(ppp) for d in ccc(qqq))
    ))
main()
