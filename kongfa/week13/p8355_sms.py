""" _ """
def main():
    """ _ """
    nokia_table = [
        "", "ABC", "DEF",
        "GHI", "JKL", "MNO",
        "PQRS", "TUV", "WXYZ"
    ]
    nnn = int(input())
    buffer = ""
    for _ in range(nnn):
        button = int(input())
        repeat = int(input())
        if button == 1:
            buffer = buffer[:-repeat]
            continue
        chars = nokia_table[button - 1]
        buffer += chars[repeat % len(chars) - 1]
    print("null" if not buffer else buffer)
main()
