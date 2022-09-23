'''PSCP Program'''
def main():
    '''Sequence VII'''
    size = int(input())
    for i in range(1, 2*size-1):
        temp = []
        for j in range(i):
            temp.append(j+1)
        if i-1 > (2*size-1)//2:
            break
        print(*temp)
    for i in range((2*size-1)//2, 0, -1):
        temp = []
        for j in range(i):
            temp.append(j+1)
        print(*temp)
    if size == 1:
        print(size)
if __name__ == "__main__":
    main()
