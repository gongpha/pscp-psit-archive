""" _ """
def main():
    """ _ """
    print([
        "Very Slow"
        if (vvv[0] and vvv[1] < 11) or (not vvv[0] and vvv[1] < 26) else
        ("Slow%s" % ("" if vvv[0] else "/Beginner"))
        if (vvv[0] and vvv[1] <= 20) or (not vvv[0] and vvv[1] <= 35) else
        ("%sAverage" % ("" if vvv[0] else "Intermediate/"))
        if (vvv[0] and vvv[1] <= 30) or (not vvv[0] and vvv[1] <= 45) else
        ("Fast%s" % ("" if vvv[0] else "/Advanced"))
        if (vvv[0] and vvv[1] <= 40) or (not vvv[0] and vvv[1] <= 65) else
        (
            "Very Fast" if vvv[0] or (not vvv[0] and vvv[1] <= 80) else "Insane"
        )
        for vvv in [(input() == "Kids", int(input()))]
    ][0])
main()
