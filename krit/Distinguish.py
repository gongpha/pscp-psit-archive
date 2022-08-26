"""Prints something to console"""
def main() -> int:
    """The main function"""
    if float(input()) > 180:
        print("You're hit the door edge.")
    else:
        print("Nothing happens.")
    return 0

if __name__ == "__main__":
    main()
