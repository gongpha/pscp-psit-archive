""" _ """
def main():
    """ _ """
    mmm = int(input())
    counter = 0
    for i in range(1, mmm + 1):
        eee = 0
        nnn = i
        if nnn % 2 == 0:
            nnn /= 2
            if nnn % 2 == 0:
                continue
        for j in range(3, int(nnn ** 0.5) + 1, 2):
            if nnn % j == 0:
                nnn /= j
                if nnn % j == 0:
                    eee = 1
                    break
        if eee:
            continue
        counter += 1
    print(counter)

main()
