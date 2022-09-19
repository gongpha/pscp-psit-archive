""" _ """
def main():
    """ _ """
    count = int(input())
    print('\n'.join([
        ' ' * abs(-(-count // 2) - i) + '*' + (
            '' if i == 1 or i == count else (('*' if -(-count // 2) == i else ' ') * (
                (count - i if i - 1 > count / 2 else (i - 1)) * 2 - 1
            ) + '*')
        )
        for i in range(1, count + 1)
    ]))
main()
