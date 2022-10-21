""" _ """
def main():
    """ _ """
    num = int(input())
    twoary = ""
    div = num
    while True:
        mod = div % 2
        div = div // 2
        twoary = str(mod) + twoary
        if div == 0:
            break
    print(twoary)

main()
