""" _ """

def semi(nnn):
    """ _ """
    pair = 0
    for i in range(2, int(nnn ** 0.5) + 1):
        while nnn % i == 0:
            nnn /= i
            pair += 1
        if pair > 1:
            break
    if nnn > 1:
        pair += 1
    return pair == 2

def main():
    """ _ """
    print(sum(semi(iii) for iii in range(1, int(input()) + 1)))
main()
