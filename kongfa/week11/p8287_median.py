""" _ """
def median(num):
    """ _ """
    nnn = len(num)
    sss = sorted(num)
    return (sss[nnn // 2] / 2 + sss[nnn // 2 - 1] / 2, sss[nnn // 2])[nnn % 2]


def main():
    """ _ """
    print("%.1f" % median([float(input()) for _ in range(int(input()))]))


main()
