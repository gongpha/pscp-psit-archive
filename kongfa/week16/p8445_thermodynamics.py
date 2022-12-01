""" _ """
from json import loads
def main():
    """ _ """
    ggg = 0
    eee = sorted(loads(input()))
    nnn = len(eee)
    nno = nnn + 1
    rrr = range(2, nno)
    def ccc():
        """ _ """
        for ppp in rrr:
            for qqq in range(0, nno - ppp):
                yyy = qqq + ppp - 1
                zzz = (eee[yyy] - eee[qqq]) // 2
                if zzz:
                    eee[qqq] += zzz
                    eee[yyy] -= zzz
                    return zzz
        return 0
    ddd = ccc()
    while ddd:
        ggg += ddd
        ddd = ccc()
    print(ggg)
main()
