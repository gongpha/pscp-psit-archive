""" _ """
def main():
    """ _ """
    raw = input().split('.')
    if len(raw) != 4:
        print('Invalid IPv4 address')
        return

    for i in raw:
        if any(map(lambda x: not x.isdigit(), i)):
            print('Invalid IPv4 address')
            return
        i = int(i)
        if i > 255 or i < 0:
            print('Invalid IPv4 address')
            return
    print('.'.join(map(lambda x: str(int(x)), raw)))
main()
