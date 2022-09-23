"""Do somthhings idk xdcc mkkas ls ba lkf"""


def main() -> int:
    """The manin fucntor"""
    range_min = int(input())
    range_max = int(input())
    input_range = tuple(filter(lambda index: index % 2 == 0,
                               range(range_min, range_max+1) if range_min < range_max else
                               reversed(range(range_max, range_min+1))))

    print("pass :", *input_range)
    print("Sum :", sum(input_range))

    return 0


if __name__ == "__main__":
    main()
