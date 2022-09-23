""" _ """

def check(aaa, bbb):
    """ _ """
    if aaa == bbb:
        return ''
    if aaa == 'R' and bbb == 'P':
        return 'P'
    if aaa == 'R' and bbb == 'S':
        return 'R'
    if aaa == 'P' and bbb == 'R':
        return 'P'
    if aaa == 'P' and bbb == 'S':
        return 'S'
    if aaa == 'S' and bbb == 'R':
        return 'R'
    if aaa == 'S' and bbb == 'P':
        return 'S'

def main():
    """ _ """
    aaaaa = 0
    bbbbb = 0
    sequence = input("")
    aaa = ''
    for sss in sequence:
        if sss in 'RPS':
            if aaa == '':
                aaa = sss
            else:
                ccc = check(aaa, sss)
                if ccc == aaa:
                    aaaaa += 1
                elif ccc == sss:
                    bbbbb += 1
                aaa = ''
    if aaaaa > bbbbb:
        print('A win %d-%d' % (aaaaa, bbbbb))
        return
    if aaaaa < bbbbb:
        print('B win %d-%d' % (bbbbb, aaaaa))
        return
    print('DRAW ' + str(aaaaa))
main()
