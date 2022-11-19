""" _ """
def main():
    """ _ """
    price = float(input())
    cap_quota = int(input())
    free = int(input())
    bottle_quota = int(input())
    free2 = int(input())
    money = float(input())
    cap = money // price
    bottle = cap
    total = cap
    while cap >= cap_quota or bottle >= bottle_quota:
        add = (cap // cap_quota) * free + (bottle // bottle_quota) * free2
        total += add
        cap = add + (cap % cap_quota)
        bottle = add + (bottle % bottle_quota)
    print(int(total))


main()
