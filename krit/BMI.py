"""Prints something to console"""


def main() -> int:
    """The main function"""
    bmi_calc()
    bmi_calc()
    bmi_calc()
    bmi_calc()
    bmi_calc()
    return 0

def bmi_calc():
    """Secondary function"""
    name, weight, height = input(), float(input()), float(input())
    print("%s's  BMI = %.2f"% (name, float(weight / ((height/100)**2))))

if __name__ == "__main__":
    main()
