""" _ """
def main():
    """ _ """
    aaa = 0
    bbb = 0
    for _ in range(10):
        aaa += int(input())
    for _ in range(10):
        bbb += int(input())
    print(
        'AB' if aaa == bbb else 'A'
        if aaa < bbb else 'B'
    )
main()
