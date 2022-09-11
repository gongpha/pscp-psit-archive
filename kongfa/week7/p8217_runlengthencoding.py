""" lz87 when ;) """
def main():
    """ _ """
    raw = input()
    out = ''
    mem = ''
    count = 0
    for ccc in raw:
        if mem == '':
            mem = ccc
        if ccc == mem:
            count += 1
        else:
            out += str(int(count)) + mem
            count = 1
            mem = ccc
    out += str(int(count)) + mem
    print(out)
main()
