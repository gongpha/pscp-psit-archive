""" _ """
import math

def main():
    """ _ """
    nnn = int(input())
    nnn += 1 if nnn % 2 != 0 else 0
    fac = math.factorial
    print(int((fac(nnn))/((fac(nnn-(nnn//2)))* (fac(nnn//2)))))
main()
