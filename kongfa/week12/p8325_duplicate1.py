""" _ """


def main():
    """ _ """
    ss1 = int(input())
    ss2 = int(input())
    sss = {input() for x in range(ss1)}.intersection(
        {input() for x in range(ss2)}
    )
    print(
        "Nope" if len(sss) == 0 else
        '\n'.join(sorted(sss, reverse=True))
    )


main()
