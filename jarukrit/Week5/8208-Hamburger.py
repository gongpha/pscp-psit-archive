'''PSCP Program'''
def main():
    '''Fizz Buzz'''
    left_bread = int(input())
    right_bread = int(input())
    print('|'*left_bread + '*'*(left_bread+right_bread)*2 + '|'*right_bread)

if __name__ == "__main__":
    main()
