""" _ """

from json import loads
def main():
    """ _ """
    aaa = loads(input())
    bbb = loads(input())

    aac = {iii : aaa.count(iii) for iii in aaa}
    bbc = {iii : bbb.count(iii) for iii in bbb}

    dff = tuple(filter(lambda x: x[1] != 0, {
        iii : abs(aac[iii] - bbc[iii] if iii in bbc and iii in aac else (
            aac[iii] if iii in aac else bbc[iii]
        ))
        for iii in set(aaa) | set(bbb)
    }.items()))

    if len(dff) == 0:
        print("ONAJI DAYO!")
        return
    for kkk, vvv in sorted(dff):
        if vvv == 0:
            continue
        print(kkk, vvv)


main()
