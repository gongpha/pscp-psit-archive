""" _ """
def main():
    """ _ """
    count = int(input())
    quota = int(input())
    stamp = int(input())
    stamp_quota = int(input())
    discount = int(input())
    total_cost = 0
    my_stamp = 0
    for _ in range(count):
        bill = int(input())
        while bill > 0 and my_stamp >= stamp_quota:
            my_stamp -= stamp_quota
            bill = max(bill - discount, 0)
        total_cost += bill
        my_stamp += stamp * (bill // quota)
    print(str(total_cost) + '\n' + str(my_stamp))
main()
