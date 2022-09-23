"""I am tired as shit"""


def main() -> int:
    """Main function"""
    size = int(input())
    for x in range(size):
        for y in range(size):
            if y == 0 or y == size-1 or x == y:
                print("*", end="")
            else:
                print(" ", end="")
        print("")  # std::endl

    return 0

if __name__ == "__main__":
    main()
