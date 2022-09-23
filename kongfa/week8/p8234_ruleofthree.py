""" _ """
def main():
    """ _ """
    count = int(input())
    best_ratio = 0
    best_price = 0
    best_size = 0
    for _ in range(count):
        price = float(input())
        capa = float(input())
        ratio = capa / price
        if ratio > best_ratio:
            best_ratio = ratio
            best_price = price
            best_size = capa
        elif ratio == best_ratio and price < best_price:
            best_price = price
            best_size = capa
    print("%.2f %.2f" % (best_price, best_size))
main()
