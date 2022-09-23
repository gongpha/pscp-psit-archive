'''PSCP Program'''
def main():
    ''' N (Not Word) '''
    size = int(input())
    for i in range(size):
        for j in range(size):
            if i == j or j == 0 or j == size-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == "__main__":
    main()
