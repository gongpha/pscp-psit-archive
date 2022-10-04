""" _ """


def main():
    """ _ """
    seq = input()
    aaa_score = 0
    bbb_score = 0
    aaa_set = 0
    bbb_set = 0
    currset = 1
    nextset = False
    for ccc in seq:
        if ccc == "A":
            aaa_score += 1
        elif ccc == "B":
            bbb_score += 1
        if abs(aaa_score - bbb_score) >= 2:
            if aaa_score >= (15 if currset == 5 else 25) and aaa_score > bbb_score:
                aaa_set += 1
                nextset = True
            if bbb_score >= (15 if currset == 5 else 25) and aaa_score < bbb_score:
                bbb_set += 1
                nextset = True
        if nextset:
            print("Set %d: A (%d) | B (%d)" % (currset, aaa_score, bbb_score))
            currset += 1
            aaa_score = 0
            bbb_score = 0
            if aaa_set >= 3 or bbb_set >= 3:
                if aaa_set > bbb_set:
                    print("A won %s:%s set" % (aaa_set, bbb_set))
                else:
                    print("B won %s:%s set" % (bbb_set, aaa_set))
                return
            nextset = False
    print(
        "Set %d: A (%d) | B (%d)\nThe game has not finished yet." % (
            currset, aaa_score, bbb_score
        )
    )


main()
