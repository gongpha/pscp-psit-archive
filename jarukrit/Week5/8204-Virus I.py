'''PSCP Program'''
def main():
    '''Virus I'''
    text, count = input(), 0
    for i in text:
        if i == 'o':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
