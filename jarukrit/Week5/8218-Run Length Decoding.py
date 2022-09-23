'''PSCP Program'''
def main():
    ''' Run Length Decoding '''
    encoded, length = input(), ''
    for i in encoded:
        if i.isnumeric():
            length += i
        elif i.isalpha():
            print(i * int(length), end="")
            length = ''

if __name__ == "__main__":
    main()
