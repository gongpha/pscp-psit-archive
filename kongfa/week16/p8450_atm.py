""" _ """
def main():
    """ _ """
    balance = int(input())
    while True:
        ttt = input()
        if ttt == "END":
            break
        ttt = ttt.split()
        if ttt[0] == "D":
            balance += int(ttt[1])
        elif ttt[0] == "W":
            balance -= min(balance, int(ttt[1]))
    print(balance)
main()
