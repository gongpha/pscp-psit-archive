""" why tf this problem has 192 cases ? """

def main(stringpool=("ABO+-{}? IMPOSSIBLE (obfuscated by it65070013 kongfa waroros)")):
    """ _ """
    print(*([
        [
            (vvv[0][0], vvv[0][1], stringpool[5] + (stringpool[8].join(
                www[0]((vvv[0][0] + vvv[0][1], vvv[1][:]))
            )) + stringpool[6]) if vvv[0][2] == stringpool[7] else
            (vvv[0][0], vvv[2]((
                vvv[0][0], vvv[0][2], vvv[1][:], www
            )), vvv[0][2]) if vvv[0][1] == stringpool[7] else
            (vvv[2]((vvv[0][1], vvv[0][2], vvv[1][:], www)), vvv[0][1], vvv[0][2])
            for vvv in [(
                input().split(),
                [
                    stringpool[0] + stringpool[3],
                    stringpool[0] + stringpool[4],
                    stringpool[1] + stringpool[3],
                    stringpool[1] + stringpool[4],
                    stringpool[0:2] + stringpool[3],
                    stringpool[0:2] + stringpool[4],
                    stringpool[2] + stringpool[3],
                    stringpool[2] + stringpool[4]
                ],
                lambda xxx: [
                    stringpool[9:19] if len(uuu) == 0 else
                    stringpool[5] + (stringpool[8].join(uuu)) + stringpool[6]
                    for uuu in [[
                        i for i in xxx[2] if xxx[1] in xxx[3][0]((xxx[0] + i, xxx[2][:]))
                    ]]
                ][0]
            )]
        ][0]
        for www in [[
            lambda ccc: [
                [ccc[1].remove(i) for i in (
                    ([
                        stringpool[0] + stringpool[3],
                        stringpool[1] + stringpool[3],
                        stringpool[0:2] + stringpool[3],
                        stringpool[2] + stringpool[3]
                    ] if (stringpool[3] not in ccc[0]) else []) +
                    ([
                        stringpool[0] + stringpool[3],
                        stringpool[0] + stringpool[4],
                        stringpool[0:2] + stringpool[3],
                        stringpool[0:2] + stringpool[4]
                    ] if (stringpool[0] not in ccc[0]) else []) +
                    ([
                        stringpool[1] + stringpool[3],
                        stringpool[1] + stringpool[4],
                        stringpool[0:2] + stringpool[3],
                        stringpool[0:2] + stringpool[4]
                    ] if (stringpool[1] not in ccc[0]) else []) +
                    ([
                        stringpool[2] + stringpool[3],
                        stringpool[2] + stringpool[4]
                    ] if (stringpool[0:2] in ccc[0]) else []) +
                    ([
                        stringpool[0:2] + stringpool[3],
                        stringpool[0:2] + stringpool[4]
                    ] if (stringpool[2] in ccc[0]) else [])
                ) if i in ccc[1]],
                ccc[1]
            ][1]
        ]]
    ][0]))
main()
