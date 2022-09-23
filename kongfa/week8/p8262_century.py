""" _ """
def main():
    """ _ """
    count = int(input())
    buffer = ""
    for i in range(count):
        what = input()
        year = 0
        if what.startswith('B.E.'):
            year = -543
        year += int(what[4:])
        buffer += (
            'ERROR' if year < 1 else str(max(1, -(-year // 100)))
        ) + ('' if i == count - 1 else '\n')
    print(buffer)
main()
