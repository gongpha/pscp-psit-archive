"""Prints something to console"""
def main() -> int:
    """The main function"""
    bmi = int(input()) / ((int(input())/100)**2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")
    return 0

if __name__ == "__main__":
    main()
