'''PSCP Program'''
def main():
    '''Left Arrow'''
    length, height = "*"*int(input()), int(input())
    for i in range(-(height // -2)-1):
        print(" "*((-(height // -2)-1)-i), length, sep="", end="")
        print()
    for i in range((height//2)+1):
        print(" "*i, length, sep="", end="")
        print()

if __name__ == "__main__":
    main()
