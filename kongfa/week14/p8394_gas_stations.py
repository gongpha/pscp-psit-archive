""" _ """

def check_dist(lll):
    """ _ """
    vvv, dist, gaps, full, iii, left = lll
    if vvv > left[0] or iii == len(gaps):
        return 0
    if vvv >= dist or (vvv < left[0] and gaps[iii + 1] <= left[0]):
        return 0
    left[0] = vvv + full
    return 1

def main():
    """ _ """
    dist = float(input())
    drive_full = float(input())
    station_gaps = [float(input()) for _ in range(int(input()))]
    station_gaps += [station_gaps[-1]] if len(station_gaps) > 0 else []
    left = [drive_full]
    enter = sum(
        check_dist((vvv, dist, station_gaps, drive_full, i, left))
        for i, vvv in enumerate(station_gaps)
    )
    print(
        "depleted" if left[0] < dist else enter
    )


main()
