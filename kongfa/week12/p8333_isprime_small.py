""" _ """
def main():
    """ _ """
    nnn = int(input())
    if nnn <= 1:
        print('No')
        return
    for i in range(2, nnn):
        if nnn % i == 0:
            print('No')
            return
    print('Yes')
    return
main()
