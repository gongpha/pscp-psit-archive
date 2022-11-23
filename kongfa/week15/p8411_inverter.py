""" _ """
def main():
    """ _ """
    binary = input()
    invert = ""
    found_one = False
    for ccc in binary:
        if ccc == '0':
            found_one = True
            invert += '1'
        else:
            if found_one:
                invert += '0'
    print(invert)

main()
