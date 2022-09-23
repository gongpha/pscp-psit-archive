'''PSCP Program'''
def main():
    '''Surprising Vote'''
    total, highest = float(input()), float(input())
    cond1 = abs(highest - ((total-(highest*2)))) > 2
    if cond1:
        if highest <= 2:
            print("Not surprising")
        else:
            print("Surprising")
    else:
        print("Not surprising")

if __name__ == "__main__":
    main()
