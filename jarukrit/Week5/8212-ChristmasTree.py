'''PSCP Program'''
def main():
    '''
    I don't want a lot for Christmas
    There is just one thing I need
    I don't care about the presents underneath the Christmas tree
    I just want you for my own
    More than you could ever know
    Make my wish come true
    All I want for Christmas is you
    '''
    leaf_size = int(input())
    stem = int(input())
    base_size = 0
    for i in range(leaf_size):
        print(" " * int(leaf_size - (i +1)), end="")
        print('*' * ((i*2)+1))
        base_size = ((i*2)+1)
    for i in range(stem):
        print('---'.center(base_size+1))
if __name__ == "__main__":
    main()
