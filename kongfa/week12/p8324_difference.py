""" _ """
def main():
    """ _ """
    nnnc = int(input())
    mmmc = int(input())
    nnn = set()
    mmm = set()
    for _ in range(nnnc):
        nnn.add(int(input()))
    for _ in range(mmmc):
        mmm.add(int(input()))
    print(*sorted(nnn.difference(mmm)), sep=' ')

main()
