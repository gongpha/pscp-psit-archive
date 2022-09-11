'''PSCP Program'''
def main():
    '''Sequence XII (I die inside)'''
    line = int(input())
    for i in range(line):
        # Prints the upper left side
        for j in range(i, -1, -1):
            print("%02d"% (line - j), end=" ")
        for j in range((line-1) - i):
            print("%02d"% ((line-1) - j), end=" ")
        # Prints the upper right side
        for j in range((line-1) - i, 0, -1):
            print("%02d"% ((line+1) - j), end=" ")
        for j in range(i):
            print("%02d"% (line - j - 1), end=" ")
        print()

    for i in range(line-2, -1, -1):
        # Prints the lower left side
        for j in range(i, -1, -1):
            print("%02d"% (line - j), end=" ")
        for j in range((line-1) - i):
            print("%02d"% ((line-1) - j), end=" ")
        # Prints the lower right side
        for j in range((line-1) - i, 0, -1):
            print("%02d"% ((line+1) - j), end=" ")
        for j in range(i):
            print("%02d"% (line - j - 1), end=" ")
        print()
    # Finally, my suffering is over.

if __name__ == "__main__":
    main()
