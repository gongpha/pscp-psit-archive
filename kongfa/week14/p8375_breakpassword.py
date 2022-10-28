""" _ """

import hashlib
def main():
    """ _ """
    hhh = input()
    for nnn in range(100000):
        if hashlib.sha512(str('%05d' % nnn).encode()).hexdigest().upper() == hhh:
            print('%05d' % nnn)
            break

main()
