""" _ """

def main():
    """ _ """
    nnn = input()
    print('PONG' if (
        int(nnn) % 3 == 0 or nnn[-1] == '3'
    ) else nnn)
main()
