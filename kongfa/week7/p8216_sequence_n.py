""" lz87 when ;) """
def main():
    """ _ """
    nnn = int(input())
    print('\n'.join([
        '*' + (' ' * (nnn - 2)) + '*' if y == 0 or y == nnn - 1 else
        '*' + (' ' * (y - 1)) + '*' + (' ' * (nnn - y - 2)) + '*'
        for y in range(nnn)
    ]))
main()
