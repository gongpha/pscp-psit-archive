'''PSCP Program'''
def main():
    ''' Run Length Decoding '''
    encoded, temp, count, first_run = input(), '', 0, True
    encoded += " "
    temp = encoded[0]
    for i in encoded:
        if first_run:
            first_run = False
        else:
            if i != temp:
                count += 1
                print(count, temp, sep="", end="")
                temp, count = i, 0
            elif i == temp:
                count += 1
                temp = i

if __name__ == "__main__":
    main()
