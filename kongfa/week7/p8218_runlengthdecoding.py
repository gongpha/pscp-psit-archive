""" lz87 when ;) """
def main():
    """ _ """
    encoded = input()
    decoded = ""
    mul = ""
    for ccc in encoded:
        if ccc.isalpha():
            decoded += int(mul) * ccc
            mul = ""
        else:
            mul += ccc
    print(decoded)

main()
