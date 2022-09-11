'''PSCP Program'''
def main() -> int:
    '''Leap year'''
    year = int(input())
    cond1 = (year % 4 == 0) and (year % 100 != 0)
    cond2 = (year % 400 == 0) and (year % 100 == 0)
    if cond1 or cond2:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == "__main__":
    main()
