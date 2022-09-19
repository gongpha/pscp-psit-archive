""" _ """

import string

def is_hex_and_rightlen(macs, lenwant):
    """ _ """
    for mmm in macs:
        if not set(mmm).issubset(string.hexdigits):
            return False
        if len(mmm) != lenwant:
            return False
    return True

def main():
    """ _ """
    mac = input()
    mactype = -1

    # 1
    macs = mac.split('-')
    if len(macs) == 6:
        if is_hex_and_rightlen(macs, 2):
            mactype = 1
    if mactype == -1:
        # 2
        macs = mac.split(':')
        if len(macs) == 6 and is_hex_and_rightlen(macs, 2):
            mactype = 2
    if mactype == -1:
        # 3
        macs = mac.split('.')
        if len(macs) == 3 and is_hex_and_rightlen(macs, 4):
            mactype = 3
    if mactype == -1:
        print("ERROR")
        return
    print("VALID", mactype)
main()
