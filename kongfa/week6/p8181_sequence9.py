""" _ """
def main():
    """ _ """
    nnn = int(input()) + 1
    print(
        '\n'.join(
            [' '.join(
                [
                    (
                        '%s01' % (' ' * (3 * (nnn - y - 1)))
                        if x == 0 else ('%02d' % (
                            x + 1 if x < y else (y * 2) - x - 1
                        ))
                    ) for x in range((y * 2) - 1)
                ]
            ) for y in range(1, nnn)]
        )
    )
main()