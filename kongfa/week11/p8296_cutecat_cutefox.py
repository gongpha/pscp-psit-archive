""" _ """


def main():
    """ _ """
    count = int(input())
    cats = {}
    foxes = {}
    beasts = {}
    for _ in range(count):
        raw = input()
        ccc = raw.split('"')
        cccc = raw.split("'")
        beasts.update({ccc[1]: ccc[3]} if len(ccc) > len(cccc) else
                      {cccc[1]: cccc[3]})
    allb = {}
    allb_after = 0
    if len([ttt for ttt in beasts.values() if "Cat" in ttt]) == 0 or "Cat01" not in beasts.values():
        allb["Garfield"] = "Cat01"
    if len([ttt for ttt in beasts.values() if "Fox" in ttt]) == 0 or "Fox01" not in beasts.values():
        allb["Fubuki"] = "Fox01"

    # idk, but these lines fix shit
    for kkk, vvv in sorted(beasts.items(), key=lambda iii: iii[1]):
        if "Fox01" not in beasts.values() and allb_after == 0 and vvv.count("Fox") > 0:
            allb["Fubuki"] = "Fox01"
            allb_after += 1
        allb[kkk] = vvv
    cats = {int(vvv[3:]): [kkk, vvv] for kkk, vvv in allb.items() if 'Cat' in vvv}
    foxes = {int(vvv[3:]): [kkk, vvv] for kkk, vvv in allb.items() if 'Fox' in vvv}
    print(
        ("Cat : %d\nFox : %d\n" % (
            len([ttt for ttt in allb.values() if "Cat" in ttt]),
            len([ttt for ttt in allb.values() if "Fox" in ttt])
        )) + '\n'.join([
            "%s : %s" % (cats[kkk][0], cats[kkk][1]) for kkk in sorted(cats)
        ]) + '\n' +
        "\n".join([
            "%s : %s" % (foxes[kkk][0], foxes[kkk][1]) for kkk in sorted(foxes)
        ])
    )


main()
