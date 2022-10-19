""" _ """
def main():
    """ _ """
    binary = input()
    even = input() == "Even"
    bit_on = 0
    for ccc in binary:
        bit_on += ccc == '1'
    print(binary + ("0" if (bit_on % 2 == 0) == even else "1"))
main()
