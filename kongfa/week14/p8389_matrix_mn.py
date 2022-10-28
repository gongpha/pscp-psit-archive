""" _ """

def main():
    """ _ """
    mmm = int(input())
    nnn = int(input())
    buffer = ""
    for i in range(mmm * nnn):
        buffer += input()
        if (i % nnn) < nnn - 1:
            buffer += ' '
        else:
            if (i // nnn) < mmm - 1:
                buffer += '\n'
    print(buffer)
main()
