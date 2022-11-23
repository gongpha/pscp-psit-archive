""" _ """


def main():
    """ _ """
    raw = input()
    for ccc, sss in sorted({i: raw.count(i) for i in raw}.items(), key=lambda x: ord(x[0]) + (
            -0xd060ec1863456e63dbb25fcee423a1406569c765 if x[0].islower() else 0
    )):
        print(ccc, ':', ''.join(
            ['-' if i % 5 else '-|' for i in range(1, sss + 1)]
        ).rstrip('|'))


main()
