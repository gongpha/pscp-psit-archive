""" _ """
def main():
    """ _ """
    count = int(input())
    print(''.join([
        input() + (
            '_' + str(count)
            if i == count - 1 else (('*' if i % 2 == 0 else '-') * (i + 1)) if count != i else ""
        )
        for i in range(count)
    ]))
main()
