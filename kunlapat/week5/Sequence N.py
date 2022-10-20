"""I am tired as shit"""


def main() -> int:
    """Main function"""
    size = int(input())
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print("")  # std::endl

    return 0

if __name__ == "__main__":
    main()
