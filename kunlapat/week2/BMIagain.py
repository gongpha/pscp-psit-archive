
"""Prints something to console"""


def main() -> int:
    """The main function"""
    bmi = float(input()) / (float(input())/100)**2

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

    return 0

if __name__ == "__main__":
    main()
