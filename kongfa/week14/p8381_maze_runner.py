""" _ """

def neighbour(xxx, mmap):
    """ _ """
    return not (
        xxx[0] < 0 or xxx[0] > 19 or xxx[1] < 0 or xxx[1] > 9 or mmap[xxx[1]][xxx[0]] not in 'YX '
    )

def main():
    """ _ """
    mmap = [
        [x for x in input()]
        for _ in range(10)
    ]

    for yyy, line in enumerate(mmap):
        if 'X' in line:
            xxx = line.index('X')
        else:
            xxx = -1
        if xxx != -1:
            queue = [(xxx, yyy, '', 8, 00, 0)]
            break

    while True:
        if len(queue) == 0:
            break
        xxx, yyy, ppp, hhh, mmm, iii = queue.pop(0)
        if mmap[yyy][xxx] not in 'YX ':
            continue
        elif mmap[yyy][xxx] == 'Y':
            break
        mmap[yyy][xxx] = '1'

        mmm += 23
        if mmm >= 60:
            mmm -= 60
            hhh += 1
        ttt = ((xxx, yyy-1, 'U'), (xxx+1, yyy, 'R'), (xxx, yyy+1, 'D'), (xxx-1, yyy, 'L'))
        for nnn in list(filter(lambda xxx: neighbour(xxx, mmap), ttt)):
            queue.append((nnn[0], nnn[1], ppp + nnn[2], hhh, mmm, iii + 1))
    print('%s\n%d\n%s' % (
        ppp,
        iii,
        ('You will make it on time!' if hhh < 18 else 'You won\'t make it on time.')
    ))
main()
