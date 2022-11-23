""" _ """
def prime(nnn, mmm):
    """ _ """
    if nnn in mmm:
        return True
    for i in range(2, int(nnn ** 0.5) + 1):
        if nnn % i == 0:
            return False
    mmm.add(nnn)
    return True

def main():
    """ _ """
    counter = 0
    mmm = set()

    for i in range(2, int(input()) + 1):
        if not prime(i, mmm):
            continue
        noo = 0
        rot = []
        cir = str(i)
        for _ in cir:
            rot.append(int(cir))
            cir = cir[1:] + cir[0]
        for rrr in rot:
            if not prime(rrr, mmm):
                noo = 1
                break
        if noo:
            continue
        counter += i

    print(counter)

main()
