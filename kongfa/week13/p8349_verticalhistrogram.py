""" _ """


def main():
    """ _ """
    ttt = input()

    chars = sorted(
        [(kkk, vvv) for kkk, vvv in {
            i: ttt.count(i) for i in ttt
        }.items()],
        key=lambda v: v[0].swapcase()
    )
    max_val = max(chars, key=lambda ttt: ttt[1])[1]

    print("%s\n    %s" % (
        '\n'.join([
            "%03d %s" % (
                max_val - i,
                ' '.join([
                    '*' if j[1] >= max_val - i else ' '
                    for j in chars
                ])
            )
            for i in range(max_val)
        ]),
        " ".join([
            i[0]
            for i in chars
        ])
    ))


main()
