'''PSCP Program'''
def main():
    '''Align'''
    size, alignment, text = int(input()), input(), input()
    if alignment == 'left':
        print(text)
    elif alignment == 'center':
        left_chk = size - len(text)
        if (left_chk % 2) == 1:
            text = ' ' + text
        print(text.center(size))
    elif alignment == 'right':
        print("{msg:>{length}}".format(length=size, msg=text))

if __name__ == "__main__":
    main()
