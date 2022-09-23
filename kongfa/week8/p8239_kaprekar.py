""" _ """

def swap(sss, aaa, bbb):
    """ _ """
    sss = list(sss)
    if int(sss[aaa] + sss[bbb]) > int(sss[bbb] + sss[aaa]):
        ddd = sss[aaa]
        sss[aaa] = sss[bbb]
        sss[bbb] = ddd
    return ''.join(sss)

def sor_t(intstr, reverse=False):
    """ _ """
    intstr = '%04d' % int(intstr)
    intstr = swap(intstr, 0, 1)
    intstr = swap(intstr, 1, 2)
    intstr = swap(intstr, 2, 3)
    intstr = swap(intstr, 0, 1)
    intstr = swap(intstr, 1, 2)
    intstr = swap(intstr, 0, 1)

    if reverse:
        intstr = intstr[::-1]
    return intstr

def main():
    """ _ """
    aaa = input()
    count = 0

    while True:
        count += 1
        eee = sor_t(aaa, True)
        fff = sor_t(aaa)

        aaa = int(fff) - int(eee) if int(fff) > int(eee) else int(eee) - int(fff)
        if aaa == 6174:
            break
        aaa = str(aaa)
    print(count)
main()
