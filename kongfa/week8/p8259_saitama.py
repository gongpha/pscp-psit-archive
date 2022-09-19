""" _ """
def main():
    """ _ """
    must_pu = int(input())
    must_su = int(input())
    must_ud = int(input())
    must_rn = int(input())
    day_pu = int(input())
    day_su = int(input())
    day_rn = int(input())
    day_ud = int(input())

    day_pu = must_pu / day_pu
    day_su = must_su / day_su
    day_ud = must_ud / day_ud
    day_rn = must_rn / day_rn
    mmm = 0
    if day_pu > mmm:
        mmm = day_pu
    if day_su > mmm:
        mmm = day_su
    if day_ud > mmm:
        mmm = day_ud
    if day_rn > mmm:
        mmm = day_rn
    print(int(-1 * mmm // 1 * -1))
main()
