""" _ """
def main():
    """ _ """
    nnn = int(input())
    print(
        '\n'.join(
            [' '.join(
                [
                    str(x + 1) for x in range(
                        y + ((nnn - 1) * y),
                        y + ((nnn - 1) * y) + nnn
                    )
                ]
            ) for y in range(nnn)]
        )
    )
main()
