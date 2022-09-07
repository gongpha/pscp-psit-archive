""" _ """
def main():
    """ _ """
    nnn = int(input())
    print(
        '\n'.join(
            [' '.join(
                [
                    (
                        '%s01' % (' ' * (2 * (nnn - y - 1)))
                        if x == 0 else ('%02d' % (x + 1))
                    ) for x in range(y + 1)
                ]
            ) for y in range(nnn)]
        )
    )
main()
