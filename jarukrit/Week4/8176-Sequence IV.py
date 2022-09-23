'''PSCP Program'''
def main():
    '''Sequence IV'''
    size = int(input())
    for i in range(0, size*size, size):
        temp = []
        for j in range(size):
            temp.append(j+i+1)
        print(*temp)

if __name__ == "__main__":
    main()
