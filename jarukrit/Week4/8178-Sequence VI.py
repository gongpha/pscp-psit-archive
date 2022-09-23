'''PSCP Program'''
def main():
    '''Sequence VI'''
    size = int(input())
    for i in range(1, size+1):
        temp = []
        for j in range(i):
            temp.append(j+1)
        print(*temp)

if __name__ == "__main__":
    main()
