'''PSCP Program'''
def main():
    '''Sequence VIII'''
    size = int(input())
    for i in range(size, 0, -1):
        temp = []
        for j in range(size-i+1):
            temp.append("%02d"% (j+1))
        for _ in range(size-len(temp)):
            temp.insert(0, "  ")
        print(*temp)
if __name__ == "__main__":
    main()
