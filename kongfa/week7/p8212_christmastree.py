""" _ """
def main():
    """ _ """
    leaf = int(input())
    log = int(input())

    for level in range(1, leaf + 1):
        print(' ' * ((leaf + 1) - level - 1), end='')
        print('*' * (level * 2 - 1))

    for level in range(1, log + 1):
        print(' ' * (leaf - 2), end='')
        print('---')



main()
