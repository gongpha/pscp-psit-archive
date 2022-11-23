""" _ """
import json
def main():
    """ _ """
    raw = input()
    quota = float(input())
    dictmap = dict(
        sorted({kkk: vvv for kkk, vvv in json.loads(raw).items() if vvv >= quota}.items())
    )
    print(
        "Nope" if len(dictmap) == 0 else
        "\n".join([
            "%s\t%.2f" % (kkk, vvv) for kkk, vvv in dictmap.items()
        ])
    )

main()
