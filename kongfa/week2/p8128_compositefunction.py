""" _ """

def fff(xxx):
    """ _ """
    return 2 * xxx

def ggg(xxx):
    """ _ """
    return xxx / 2 + 1

def main():
    """ _ """
    xxx = int(input())
    print("%.2f" % fff(ggg(xxx)))
    print("%.2f" % ggg(fff(xxx)))


main()
    