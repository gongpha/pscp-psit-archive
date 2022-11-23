""" _ """

def main():
    """ _ """
    cond = []
    while True:
        iii = input()
        if iii == "END":
            break
        cond.append(iii.split())

    print(*tuple(
        filter(lambda x: not any(
            {
                '>': lambda x, y: x > y,
                '<': lambda x, y: x < y,
                '=': lambda x, y: x == y,
            }[ccc[0]](x, int(ccc[1])) == (ccc[2] == 'NO') for ccc in cond
        ), range(0, 101))
    ))

main()
