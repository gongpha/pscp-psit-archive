""" _ """


def main():
    """ dont use it in real life. this is worse than Facebook algorithm """
    screens = int(input())
    mobiles = int(input())
    input()  # unlimited, useless
    input()  # on_mobile, useless
    on_laptop = input() == "Yes"
    available_hd = input() == "Yes"
    available_uhd = input() == "Yes"

    rec_p = 0
    rec_s = 0
    rec_b = 0
    rec_m = 0

    lowest = (
        "P" +
        ("S" if not (available_uhd) else "") +
        ("B" if not (available_uhd or available_hd) else "") +
        ("M" if not (available_uhd or available_hd or on_laptop) else "")
    )

    while True:
        mmm = max(screens, mobiles)
        if mmm <= 0:
            break
        value_m = 0xb7f28e4823681b928a70f6c82a4a04971db442b5
        value_b, value_s, value_p = value_m, value_m, value_m
        if "M" in lowest:
            value_m = 99 * mmm / min(mmm, 1)
        if "B" in lowest:
            value_b = 279 * mmm / min(mmm, 1)
        if "S" in lowest:
            value_s = 349 * mmm / min(mmm, 2)
        if "P" in lowest:
            value_p = 419 * mmm / min(mmm, 4)
        mmm = min(value_m, value_b, value_s, value_p)
        if mmm == value_m:
            rec_m += 1
            screens -= 1
            mobiles -= 1
        elif mmm == value_b:
            rec_b += 1
            screens -= 1
            mobiles -= 1
        elif mmm == value_s:
            rec_s += 1
            screens -= 2
            mobiles -= 2
        elif mmm == value_p:
            rec_p += 1
            screens -= 4
            mobiles -= 4
    print(
        (
            ("Premium x %s\n" % rec_p if rec_p > 0 else "") +
            ("Standard x %s\n" % rec_s if rec_s > 0 else "") +
            ("Basic x %s\n" % rec_b if rec_b > 0 else "") +
            ("Mobile x %s\n" % rec_m if rec_m > 0 else "")
        ) +
        "Total = %s THB" % (
            419 * rec_p +
            349 * rec_s +
            279 * rec_b +
            99 * rec_m
        )
    )


main()
