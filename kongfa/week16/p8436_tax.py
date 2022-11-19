""" _ """
def main():
    """ _ """
    usage_year = int(input())
    vcc = int(input())
    res = (
        vcc / 2
        if vcc <= 600 else
        ((vcc - 600) * 1.5) + (300)
        if vcc <= 1800 else
        ((vcc - 1800) * 4) + (300 * 7)
        if vcc > 1800 else 0
    )
    dis = {
        6: 0.9,
        7: 0.8,
        8: 0.7,
        9: 0.6,
    }
    if usage_year >= 6:
        if usage_year in dis:
            res *= dis[usage_year]
        elif usage_year >= 10:
            res *= 0.5

    print("%.2f" % res)

main()
