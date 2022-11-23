""" _ """
def main():
    """ _ """
    nnn = int(input())
    numdict = {
        0: 'zezeso',
        1: 'papan',
        2: 'dogugu',
        3: 'gushigi',
        4: 'zugogo',
        5: 'zugagi',
        6: 'gibugu',
        7: 'gezun',
        8: 'gegido',
        9: 'bagin',
    }
    mul = 0
    mulg = []
    while nnn > 9:
        mul += 1
        mmm = nnn % 9
        if mmm > 0:
            mulg.insert(0, mmm)
            nnn -= mmm
        nnn //= 9
    print("do ".join([
        "bagingu " * (mul - iii) + numdict[vvv]
        for iii, vvv in enumerate([nnn] + mulg)
    ]).replace('gu papan', ''))
main()
