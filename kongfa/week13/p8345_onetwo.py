""" _ """

def onetwo(num):
    """ _ """
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    return onetwo(num - 1) + onetwo(num - 2)

def main():
    """ _ """
    num = int(input())
    newstring = onetwo(num)
    print(newstring)

main()
