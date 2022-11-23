""" _ """
def main():
    """ _ """
    piv = 3.1416
    buffer = []
    sss, nnn = tuple(map(int, input().split(' ')))
    for _ in range(nnn):
        coord = tuple(map(int, input().split(' ')))
        length = (coord[0]**2 + coord[1]**2) ** 0.5
        if length == 0:
            buffer.append("0")
            continue
        near = int(-1 * ((piv * (length ** 2) - sss) / sss + 1) // 1 * -1)
        buffer.append(str(near))
    print('\n'.join(buffer))
main()
