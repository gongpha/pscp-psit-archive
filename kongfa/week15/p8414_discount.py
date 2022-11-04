""" _ """

def main():
    """ _ """
    books = []
    while True:
        iii = input()
        if iii == 'ENTER':
            break
        books.append(int(iii))

    books.sort()

    print(
        sum(books) if len(books) < 6 else
        sum(books[1:]) if len(books) < 12 else
        sum(books[2:]) if len(books) < 20 else
        sum(books[len(books) // 5:])
    )

main()
