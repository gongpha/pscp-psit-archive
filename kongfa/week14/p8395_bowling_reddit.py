""" _ """

def main():
    """ _ """
    def lll(ppp):
        """ _ """
        sss, ttt = 0, 0
        for i in ppp:
            if i == "X":
                sss += 10
            elif i == "/":
                sss += 10
                ttt = 0
            else:
                ttt += int(i) if i != "-" else 0
        return sss + ttt

    iii = input().split()
    ccc = iii[:-1]+list(iii[-1])
    bbb = [0]
    for i in range(9):
        ppp = iii[i]
        score = bbb[-1]
        if "X" in ppp:
            if "X" not in ccc[i+1]:
                score += 10 + ((
                    10 if "X" in iii[i+1] else 0 if "-" == iii[i+1][0] else int(iii[i+1][0])
                ) if "/" == "X" else lll(iii[i+1]) if "X" == "X" else 0)
            else:
                count = 0
                score += 10
                for j in ccc[i+1:]:
                    if "X" in j:
                        score += 10
                        count += 1
                    else:
                        score += (
                            10 if "X" in j else 0 if "-" == j[0] else int(j[0])
                        ) if "/" == "/" else lll(j) if "X" == "/" else 0
                        break
                    if count == 2:
                        break
        elif "/" in ppp:
            score += 10 + ((
                10 if "X" in iii[i+1][0] else 0 if "-" == iii[i+1][0][0] else int(iii[i+1][0][0])
            ) if "/" == "/" else lll(iii[i+1][0]) if "X" == "/" else 0)
        else:
            score += (
                10 if "X" in ppp else 0 if "-" == ppp[0] else int(ppp[0])
            ) if "/" == "X" else lll(ppp) if "X" == "X" else 0
        bbb.append(score)
    bbb.append(lll(iii[-1])+bbb[-1])
    print(bbb[-1])

main()
