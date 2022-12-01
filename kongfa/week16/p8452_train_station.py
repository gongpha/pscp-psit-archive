""" _ """
def main():
    """ _ """
    def lll2int(lll):
        """ _ """
        return int(lll[0]) + (float(lll[1]) / 60)
    lll = [
        [
            lll2int(jjj.split('.'))
            for jjj in iii.strip()[1:-1].split(', ')
            if jjj != ''
        ]
        for iii in [input(), input()]
    ]

    level = []
    for kkk in range(len(lll[0])):
        aaa = lll[0][kkk]
        bbb = lll[1][kkk]
        level.append((aaa, 0))
        level.append((bbb, 1))
    level.sort(key=lambda x: (x[0] * 1000) + x[1])

    platform = 0
    uod = 0

    for i in level:
        if i[1] == 0:
            uod += 1
        else:
            uod -= 1
        platform = max(platform, uod)
    print(platform)
main()
