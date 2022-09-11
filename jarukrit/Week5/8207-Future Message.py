'''PSCP Program'''
def main():
    '''Future Message'''
    text = input()
    if text.isnumeric():
        print('Number')
    elif text.isupper():
        print('Uppercase')
    elif text.islower():
        print('Lowercase')
    elif text.istitle():
        print('Title')
    elif text.isspace():
        print('Space')
    else:
        print('Other')

if __name__ == "__main__":
    main()
