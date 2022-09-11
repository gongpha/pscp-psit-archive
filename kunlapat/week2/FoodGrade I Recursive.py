"""Count the amount of chicken wings that is 50-70 grams in a pile of 24 wings"""

def grading(wings: int) -> int:
    """recusive function that counts n chickens and \
    return the amount of wings that is in range of 50-70 grams"""
    if wings > 0:
        return grading(wings-1) + int(abs(int(input()) - 60) <= 10)
    else:
        return 0


def main() -> int:
    """the main function"""
    print(grading(24))
    return 0

if __name__ == "__main__":
    main()
