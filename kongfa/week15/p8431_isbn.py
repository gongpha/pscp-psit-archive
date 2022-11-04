""" _ """
def main():
    """ _ """
    isbn = input().replace('-', '').replace(' ', '')
    check = 0
    for iii in range(9):
        check += ((10 - iii) * int(isbn[iii]))
    check = -check % 11

    if check == (int(isbn[9]) if isbn[9] != 'X' else check):
        print("Yes")
    else:
        if check >= 10:
            check = "X"
        print("No %s" % str(check))

main()
