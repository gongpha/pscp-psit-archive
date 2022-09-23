'''PSCP Program'''
def main():
    '''Sequence I'''
    size = int(input())
    for _ in range(size):
        temp = []
        for i in range(size):
            temp.append(i+1)
        print(*temp)


if __name__ == "__main__":
    main()
