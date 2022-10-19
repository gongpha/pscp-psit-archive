""" _ """
def main():
    """ _ """
    print('\n'.join([
        '\n'.join("%d %d" % (x[0], x[1]) for x in sorted(
            sorted(
                [
                    [int(x) for x in input().split()]
                    for _ in range(int(input()))
                ], key=lambda x: x[1], reverse=True
            ), key=lambda x: x[0] + x[1]
        ))
        for _ in range(int(input()))
    ]))
main()
