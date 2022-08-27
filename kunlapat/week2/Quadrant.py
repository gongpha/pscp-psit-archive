"""Prints something to console"""
def main() -> int:
    """The main function"""
    location = (float(input()), float(input()))
    if location[0] == 0 and location[1] == 0:
        print("O")
    elif location[1] == 0:
        print("X")
    elif location[0] == 0:
        print("Y")
    elif location[0] > 0 and location[1] > 0:
        print("Q1")
    elif location[0] < 0 and location[1] > 0:
        print("Q2")
    elif location[0] < 0 and location[1] < 0:
        print("Q3")
    elif location[0] > 0 and location[1] < 0:
        print("Q4")

    return 0

if __name__ == "__main__":
    main()
