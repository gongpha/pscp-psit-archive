""" _ """

# fucc "min" is not allowed


def advance_m_inute(mmm, hhh):
    """ _ """
    mmm = "%02d" % (int(mmm) + 1)
    if mmm == "60":
        mmm = "00"
        hhh = str(int(hhh) + 1)
        if hhh == "24":
            hhh = "0"
    return mmm, hhh


def main():
    """ _ """
    nnn = int(input())
    clock = input()
    hhh = ""
    mmm = ""
    later = False
    for ccc in clock:
        if ccc == ":":
            later = True
        else:
            if later:
                mmm += ccc
            else:
                hhh += ccc
    mmm, hhh = advance_m_inute(mmm, hhh)
    while nnn > 0:
        palin = (
            (
                hhh[0] == mmm[1]
            ) if len(hhh) == 1 else (
                hhh[0] == mmm[1] and
                hhh[1] == mmm[0]
            )
        )

        if palin:
            print("%s:%s" % (hhh, mmm))
            nnn -= 1
        mmm, hhh = advance_m_inute(mmm, hhh)


main()
