""" _ """


def main():
    """ _ """
    buffer = []
    while True:
        nnn = int(input())
        if nnn == 0:
            break
        count = 1
        while nnn != 1:
            nnn = nnn // 2 if nnn % 2 == 0 else nnn * 3 + 1
            count += 1
        buffer.append(str(count))
    print('\n'.join(buffer))


main()
