""" _ """
def main():
    """ _ """
    nnn = int(input())
    print(
        '\n'.join(
            [' '.join(
                [
                    (
                        '%s01' % (' ' * (3 * abs(nnn - y)))
                        if x == 0 else ('%02d' % (
                            x + 1 if x < (y if y <= nnn else nnn * 2 - y) else (
                                (y if y <= nnn else nnn * 2 - y) * 2
                            ) - x - 1
                        ))
                    ) for x in range((y * 2) - 1 if y <= nnn else ((nnn * 2 - y) * 2) - 1)
                ]
            ) for y in range(1, nnn * 2)]
        )
    )
main()
