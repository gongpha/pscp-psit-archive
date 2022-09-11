'''PSCP Program'''
def main():
    '''Sequence V'''
    size = int(input())
    temp = []
    for i in range(0, -(size // -7)):
        temp = []
        for j in range(7):
            if (size-j-(i*7)) == 0:
                break
            temp.append(size-j-(i*7))
        print(*temp)

if __name__ == "__main__":
    main()
