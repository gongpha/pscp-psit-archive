""" _ """
def main():
    """ _ """
    print(
        '\n'.join(
            [' '.join(
                [
                    str(x + 1) for x in range(y + 1)
                ]
            ) for y in range(int(input()))]
        )
    )
main()