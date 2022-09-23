""" _ """
def main():
    """ _ """
    log = ""
    while True:
        login = input()
        if login == 'END':
            break
        log += login
    print(log.count('CP'))
main()
