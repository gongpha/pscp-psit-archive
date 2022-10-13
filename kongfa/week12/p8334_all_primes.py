""" _ """
def main():
    """ _ """
    mprime = int(input())
    total = 0
    for i in range(2, mprime + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            total += 1
    print(total)
main()
