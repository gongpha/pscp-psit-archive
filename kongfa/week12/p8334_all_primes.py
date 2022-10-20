""" _ """
def main():
    """ _ """
    print(sum([1 for i in range(2, int(input()) + 1) if all(i % j != 0 for j in range(2, i))]))
main()
