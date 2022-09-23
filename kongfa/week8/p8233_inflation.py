""" _ """
def main():
    """ _ """
    price = int(float(input()) * 100)
    year = int(input())
    for _ in range(year):
        price += (price * 381) // 10000
    print("%d.%02d" % (price // 100, price % 100))
main()
