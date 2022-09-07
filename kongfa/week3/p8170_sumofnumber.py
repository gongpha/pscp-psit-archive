""" _ """
def main():
    """ _ """

    sumt = int(input())
    sumn = 0
    while True:
        sumc = int(input())
        if sumc == -1:
            break
        sumn += sumc
        if sumt == sumn:
            break
    print(sumn)
main()
