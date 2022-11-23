""" _ """
def main():
    """ _ """
    prev = 0
    total = 0
    for i in map(int, input().split()):
        total += abs(i - prev)
        prev = i
    print(total)
main()
