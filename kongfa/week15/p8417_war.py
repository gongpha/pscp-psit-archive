""" _ """
from json import loads
def main():
    """ _ """
    def iii(vvv):
        """ _ """
        vvv[2] += 1
    print([
        sum(
            (vvv[0][vvv[2]], iii(vvv))[0]
            for ddd in range(len(vvv[1]))
            if vvv[1][ddd] < vvv[0][vvv[2]]
        )
        for vvv in [
            [sorted(loads(input()), reverse=True), sorted(loads(input()), reverse=True), 0]
        ]
    ][0])
main()
