""" Something Something"""


def main() -> int:
    """Main Function"""
    bun_top = int(input())
    bun_bottom = int(input())

    print("|"*bun_top, "*"*(bun_top+bun_bottom)*2, "|"*bun_bottom, sep="")

    return 0

if __name__ == "__main__":
    main()
