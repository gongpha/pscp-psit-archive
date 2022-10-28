""" _ """

def main():
    """ _ """
    nnn = int(input())
    nns = [int(input()) for _ in range(nnn)]
    while len(nns) != 1:
        nnn1 = nns[0]
        nnn2 = nns[1]
        while nnn2:
            nnn1, nnn2 = nnn2, nnn1 % nnn2
        nns.pop(0)
        nns.pop(0)
        nns.append(nnn1)
    print(nns[0])
main()
