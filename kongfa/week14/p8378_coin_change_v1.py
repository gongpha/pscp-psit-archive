""" _ """
def main():
    """ _ """
    change = int(input())
    c25 = change // 25
    left = change % 25
    c10 = left // 10
    left = left % 10
    cc5 = left // 5
    cc1 = left % 5
    print(c25 + c10 + cc5 + cc1)

main()
