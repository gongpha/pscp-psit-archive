""" _ """
import json


def main():
    """ _ """
    print("\n".join([
        str(x)[-1]
        for x in json.loads(input())
    ]))


main()
