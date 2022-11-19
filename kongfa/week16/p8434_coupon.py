""" _ """
def main():
    """ _ """
    cost = float(input())
    cou1 = cost
    cou2 = cost
    coupon1 = list(map(float, input().split()))
    coupon2 = list(map(float, input().split()))
    if cost >= coupon1[1]:
        cou1 = max(cost - coupon1[0], 0.0)
    if cost >= coupon2[1]:
        cou2 = max(cost * (100.0 - coupon2[0]) / 100.0, 0.0)
    print('Nope' if cou1 == cou2 == cost else (
        "%d %.1f" % (
            1 if (coupon1[1] <= coupon2[1] if cou1 == cou2 else (
                cou1 < cou2
            )) else 2,
            cou1 if cou1 < cou2 else cou2
        )
    ))

main()
