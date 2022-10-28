""" _ """
import json
def main():
    """ _ """
    aaa, bbb = {}, {}
    for iii in json.loads(input()):
        aaa[iii] = aaa.get(iii, 0) + 1
    for iii in json.loads(input()):
        bbb[iii] = bbb.get(iii, 0) + 1
    ppp = int(input())
    print(sum(
        bbb[ppp - kkk] * aaa[kkk]
        for kkk in sorted(aaa.keys())
        if kkk <= ppp and ppp - kkk in bbb
    ))
main()
