""" _ """

def main():
    """ _ """
    input()
    keep = list(map(int, input().split()))
    day = 0

    while 0 not in keep:
        _, iii = min((vvv, iii) for (iii, vvv) in enumerate(keep))
        keep = list(
            map(lambda ttt: ttt[1] - 1 if ttt[0] != iii else ttt[1], enumerate(keep))
        )
        day += 1
    print(day)

main()
