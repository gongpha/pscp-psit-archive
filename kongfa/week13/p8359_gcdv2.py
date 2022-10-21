""" recycle from gcdv1 """
def main():
    """ _ """
    nnn1 = int(input())
    nnn2 = int(input())
    while nnn2:
        nnn1, nnn2 = nnn2, nnn1 % nnn2
    print(nnn1)
main()
