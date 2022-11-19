""" _ """
def main():
    """ _ """
    lll = []
    while True:
        vvv = input()
        if vvv == "END":
            break
        lll.append(int(vvv))

    def qqq(arr, lll, rrr):
        """ MY DARLING QUICKSORT (/ >//3//<)/ """
        def ppp(arr, lll, rrr):
            """ _ """
            iii = arr[rrr]
            jjj = lll - 1
            for kkk in range(lll, rrr):
                if arr[kkk] <= iii:
                    jjj = jjj + 1
                    (arr[jjj], arr[kkk]) = (arr[kkk], arr[jjj])
            arr[jjj + 1], arr[rrr] = arr[rrr], arr[jjj + 1]
            return jjj + 1
        if lll < rrr:
            vvv = ppp(arr, lll, rrr)
            qqq(arr, lll, vvv - 1)
            qqq(arr, vvv + 1, rrr)

    qqq(lll, 0, len(lll) - 1)
    print('\n'.join(map(str, lll)))
main()
