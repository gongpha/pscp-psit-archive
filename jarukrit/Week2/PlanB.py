"""Prints something to console"""
def main() -> int:
    """The main function"""
    if float(input()) >= 450:
        print("Pass")
    else:
        print("Fail")
    print("Process is terminated")
    return 0

if __name__ == "__main__":
    main()
