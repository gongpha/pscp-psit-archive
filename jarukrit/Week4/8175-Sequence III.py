'''PSCP Program'''
def main():
    '''Sequence III'''
    size = int(input())
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(j+2+i)
        print(*temp)

if __name__ == "__main__":
    main()
