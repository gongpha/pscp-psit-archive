""" _ """

def main():
    """ _ """
    result = []
    while True:
        otp = input()
        if otp == '0':
            break
        ccc = {e:otp.count(e) for e in set(otp)}
        cond = (
            (4, (2, -1), (1, -1)),
            (6, (2, 3), (2, 1)),
            (8, (2, 3), (3, 2)),
        )

        resultt = 'Invalid'

        for cnd in cond:
            countsub1 = 0
            countsub2 = 0
            if len(otp) == cnd[0]:
                for _, vvv in ccc.items():
                    if vvv == cnd[1][0]:
                        countsub1 += 1
                    elif vvv == cnd[1][1]:
                        countsub2 += 1
                if countsub1 == cnd[2][0] or countsub2 == cnd[2][1]:
                    resultt = 'Valid'
                break
        result.append(resultt)
    print(*result, sep='\n')
main()
