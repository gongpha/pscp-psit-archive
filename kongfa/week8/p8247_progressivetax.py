""" _ """
def main():
    """ _ """
    thaitaxes = (
        (4000000, 0.35),
        (2000000, 0.30),
        (1000000, 0.25),
        (750000, 0.20),
        (500000, 0.15),
        (300000, 0.10),
        (150000, 0.05),
    )
    income = float(input())
    tax = 0

    for pair in thaitaxes:
        if income > pair[0]:
            cut = income - pair[0]
            tax += int(cut * pair[1])
            income -= cut
    print(tax)
main()
