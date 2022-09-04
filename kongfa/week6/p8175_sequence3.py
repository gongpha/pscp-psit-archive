""" _ """
def main():
    """ _ """
    nnn = int(input())
    print('\n'.join([' '.join([str(x) for x in range(y + 2, nnn + 2 + y)]) for y in range(nnn)]))
main()
