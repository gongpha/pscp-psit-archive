""" Something Something"""

def main() -> int:
    """Main Function"""
    leaves = int(input())
    trunk = int(input())

    width = leaves * 2 - 1

    # render tree leaves
    for index in range(1, leaves+1):
        print(("*"*((index*2)-1)).center(width))

    # render tree trunk
    for _ in range(trunk):
        print(("---").center(width))

    return 0

if __name__ == "__main__":
    main()
