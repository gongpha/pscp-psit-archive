""" _ """


def main():
    """ _ """
    nnn = [str(y) for y in list(filter(
        lambda x: int(x) % 3 == 0 or int(x) % 5 == 0, input().split()[::-1]
    ))]
    print("Nope" if len(nnn) == 0 else "\n".join(nnn))


main()
