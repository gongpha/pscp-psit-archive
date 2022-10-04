""" _ """
def main():
    """ _ """
    price = int(input())
    cap_quota = int(input())
    new_price = int(input())
    want = int(input())

    cost = 0
    cap = 0
    curr_price = price

    while want > 0:
        cap += 1
        cost += curr_price
        curr_price = price
        if cap == cap_quota:
            curr_price = new_price
            cap = 0
        want -= 1
    print(cost)
main()
