""" _ """

def main():
    """ _ """
    nnn = int(input())

    print('\n'.join([
        ' '.join([
            '%02d' % min(
                y if y <= nnn else nnn + (nnn - y),
                x if x <= nnn else nnn + (nnn - x)
            )
            for x in range(1, nnn * 2)
        ])
        for y in range(1, nnn * 2)
    ]))

main()
