""" _ """

def main():
    """ _ """
    weight = int(input()) # kg
    height = int(input()) / 100 # m

    bmi = weight / height**2

    print(
        "Underweight" if bmi < 18.5 else
        "Normal" if bmi < 25 else
        "Overweight" if bmi < 30 else "Obese"
    )

main()
