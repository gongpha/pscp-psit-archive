""" _ """
import json


def main():
    """ _ """
    nnn = list(filter(lambda x: x % 2 == 0, json.loads(input())))
    print("Nope" if len(nnn) == 0 else ('\n'.join([str(x) for x in nnn])))


main()
