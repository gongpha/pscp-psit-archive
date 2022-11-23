""" _ """
def main():
    """ _ """
    nnn = int(input())
    print('YES' if nnn > 1 and all(nnn % i for i in range(2, int(nnn**0.5)+1)) else 'NO')
main()
