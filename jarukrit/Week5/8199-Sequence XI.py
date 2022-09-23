'''PSCP Program'''
def main():
    '''Sequence XI'''
    line = int(input())
    for i in range(1, line+1):
        for j in range(i):
            print("%02d" % (j+1), end=" ")
        for j in range(line - i):
            print("%02d" % (i), end=" ")

        for j in range(line - i, 0, -1):
            print("%02d" % (i), end=" ")
        for j in range(i-2, -1, -1):
            print("%02d" % (j+1), end=" ")
        print()

    for i in range(line-1, 0, -1):
        for j in range(i):
            print("%02d" % (j+1), end=" ")
        for j in range(line - i):
            print("%02d" % (i), end=" ")

        for j in range(line - i, 0, -1):
            print("%02d" % (i), end=" ")
        for j in range(i-2, -1, -1):
            print("%02d" % (j+1), end=" ")

        print()

if __name__ == "__main__":
    main()
