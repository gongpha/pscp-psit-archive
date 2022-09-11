'''PSCP Program'''
def main():
    '''Sequence IX'''
    size = int(input())
    count = size - 1
    for i in range(size, 0, -1):
        for _ in range(count, 0, -1):
            print("  ", end=" ")
        count -= 1

        for j in range(size-i+1):
            print("%02d" % (j+1), end=" ")

        for j in range(size-i):
            print("%02d" % ((size-i) - j), end=" ")
        print()

if __name__ == "__main__":
    main()
