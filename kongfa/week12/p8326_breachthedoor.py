""" _ """


def main():
    """ _ """
    print(' '.join(
        filter(lambda a: len(a) > 6, (
            [''.join(filter(str.isalpha, i)) for i in input().split(" ")]
        ))
    ))
main()
