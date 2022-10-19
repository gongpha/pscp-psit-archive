""" _ """


def main():
    """ _ """
    count = int(input())
    buffer = []
    for _ in range(count):
        time = int(input())
        bookcount = int(input())
        books = [int(input()) for x in range(bookcount)]
        books.sort()
        read = 0
        used = 0
        for bbb in books:
            if used + bbb > time:
                break
            used += bbb
            read += 1
        buffer.append(str(read))
    print('\n'.join(buffer))


main()
