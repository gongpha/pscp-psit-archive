""" _ """
def main():
    """ _ """
    size = int(input())
    count = int(input())
    print('\n'.join([' '.join([
        "*" * size if y == 0 or y == size - 1 else
        '*' + (
            ' ' * ((size // 2) - 1)
        ) + '*' + (
            ' ' * ((size // 2) - 1)
        ) + '*' if y == size // 2 else
        '*' + (
            ' ' * ((y - 1) if y < size // 2 else (size - y) - 2) +
            '*' +
            ' ' * ((((size // 2) - (y if y < size // 2 else (size - y) - 1)) * 2 - 1)) +
            '*' +
            ' ' * ((y - 1) if y < size // 2 else (size - y) - 2)
        ) + '*'
        for x in range(count)
    ]) for y in range(size)]))
main()
