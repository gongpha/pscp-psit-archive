""" _ """
def main():
    """ _ """
    bbb1 = input()
    chips = input()
    bbb2 = input()
    get = int(input())

    in_chips = chips.count(')')
    get_chips = chips[:get].count(')')
    left = in_chips - get_chips
    print(get_chips)
    print("None." if left == 0 else "There are still some left.")
    print(bbb1)
    print(get * ' ' + chips[get:])
    print(bbb2)
main()
