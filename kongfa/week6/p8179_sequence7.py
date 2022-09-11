""" _ """
def main():
    """ _ """
    nnn = int(input())
    print(
        '\n'.join(
            [' '.join(
                [
                    str(x + 1) for x in range(y + 1 if y < nnn else (nnn * 2 - y - 1))
                ]
            ) for y in range(nnn * 2 - 1)]
        )
    )
main()
