""" _ """
def main():
    """ _ """
    nnn = int(input())
    print(
        '\n'.join(
            [' '.join(
                [
                    str(x) for x in range(
                        nnn - (y * 7),
                        max(0, nnn - ((y + 1) * 7)),
                        -1
                    )
                ]
            ) for y in range(-(-nnn // 7))]
        )
    )
main()
