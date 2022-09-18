""" _ """
def main():
    """ fucc enum """
    day_type = input()
    age = float(input())
    height_cm = float(input())
    print("FREE" if (age < 14 and height_cm < 90) or (
        day_type == "Children Day" and
        (age < 14 and height_cm <= 140)
    ) or (
        day_type == "Senior Day" and
        age >= 60
    ) else "PAY")
main()
