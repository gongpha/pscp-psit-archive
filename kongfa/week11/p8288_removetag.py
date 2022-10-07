""" _ """


def main():
    """ _ """
    print([
        item for sublist in [
            x[1].split()
            for x in list(filter(
                lambda x: x[0] % 2 == 0 and x[1] != '', enumerate(
                    input().replace('<', '\001').replace('>', '\001').split('\001'))
            ))
        ] for item in sublist
    ])


main()
