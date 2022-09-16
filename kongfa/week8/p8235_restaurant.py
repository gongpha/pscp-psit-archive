""" _ """
def main():
    """ _ """
    bill = float(input())
    quota = float(input())
    discount_percent = float(input())
    more = float(input())

    calc = (bill + more) * (100 - discount_percent) / 100
    if bill == quota:
        bill = bill * (100 - discount_percent) / 100
    print(
        ("No %.3f" % (calc - bill)) if bill < calc else ("Yes %.3f" % (bill - calc))
        if bill > calc else "Yes"
    )
main()
