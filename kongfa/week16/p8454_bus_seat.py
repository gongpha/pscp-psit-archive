""" _ """
def main():
    """ _ """
    nnn = list(map(int, (input(), input(), input())))
    stream = [[]]
    for iii in range(nnn[0], 0, -1):
        stream[-1] += [
            'XX' if jjj == nnn[2] else "%0.2d" % jjj
            for jjj in range(iii, (nnn[0] * nnn[1]) + 1, nnn[0])
        ]
        stream += [[]] + ([[]] if iii % 2 != 0 and iii != 1 else [])
    if stream[-1] == []:
        stream.pop()
    print('\n'.join(
        ' '.join(i)
        for i in stream
    ))
main()
