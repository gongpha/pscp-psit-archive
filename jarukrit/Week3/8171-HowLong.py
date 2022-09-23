'''PSCP Program'''
def main() -> int:
    '''HowLong'''
    my_string = input().replace('-', '')
    co_unt = 0
    for _ in my_string:
        co_unt += 1
    print(co_unt)
    return 0

if __name__ == "__main__":
    main()
