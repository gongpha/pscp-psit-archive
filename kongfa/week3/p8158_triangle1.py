""" _ """
def main():
    """ _ """
    xxx = float(input())
    yyy = float(input())
    zzz = float(input())

    best = xxx
    aaa = yyy
    bbb = zzz
    if best < yyy:
        best = yyy
        aaa = xxx
        bbb = zzz
    if best < zzz:
        best = zzz
        aaa = xxx
        bbb = yyy

    diff = abs((aaa**2 + bbb**2) - best**2) < 0.01

    print(
        "Yes" if diff else "No"
    )

main()
