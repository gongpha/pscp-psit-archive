""" _ """
def main(stringpool=("No", "Yes")):
    """ _ """
    def ggg(vvv, xxx):
        """ _ """
        ccc = [xxx[2], xxx[3]]
        while ccc[0] != xxx[7] and ccc[1] != xxx[8]:
            vvv[0].append((ccc[0], ccc[1]))
            ccc = (ccc[0] + vvv[1], ccc[1] + vvv[2])
    print(
        [
            stringpool[0] if abs(xxx[7] - xxx[2]) != abs(xxx[8] - xxx[3]) else
            stringpool[1] if (xxx[7] == xxx[4] and xxx[8] == xxx[5] and xxx[6] == 1) else
            stringpool[0] if (xxx[7] == xxx[4] and xxx[8] == xxx[5] and xxx[6] == 0) else
            [
                (ggg(vvv, xxx), stringpool[0] if (xxx[4], xxx[5]) in vvv[0] else stringpool[1])[1]
                for vvv in [
                    ([], -1 if xxx[7] - xxx[2] < 0 else 1, -1 if xxx[8] - xxx[3] < 0 else 1)
                ]
            ][0]
            for xxx in [tuple([int(input()) for _ in range(9)])]
        ]
        [0]
    )
main()
