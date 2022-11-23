""" _ """
def main():
    """ _ """
    nnn = int(input())
    if nnn < 2:
        print(False)
        return
    for iii in range(2, int(nnn**0.5) + 1, 3):
        if nnn % iii == 0:
            print(False)
            return
    print(True)
main()
