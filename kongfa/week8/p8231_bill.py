""" _ """
def main():
    """ _ """
    price = float(input())
    print("%.2f" % ((price + max(50, min(price * 0.1, 1000))) * 1.07))
main()
