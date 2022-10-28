""" _ """

def main():
    """ _ """
    baht = int(input())
    rate = float(input())
    for _ in range(int(input())):
        total = (baht * rate) / 100
        baht += total
    print('%.2f' % baht)
main()
