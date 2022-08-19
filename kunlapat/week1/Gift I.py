"""prints user input to console"""


def main() -> int:
    """the main function"""

    gift_m = float(input())
    gift_k = float(input())
    print(gift_m*2-gift_k)
    return 0

if __name__ == "__main__":
    main()
