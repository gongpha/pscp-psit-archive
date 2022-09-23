'''PSCP Program'''
def main():
    '''Sequence II'''
    size, temp = int(input()), []
    for i in range(size):
        temp.append((i+1)**2)
    print(*temp)

if __name__ == "__main__":
    main()
