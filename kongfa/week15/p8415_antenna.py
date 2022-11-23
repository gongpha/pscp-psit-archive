""" _ """

from json import loads
def main():
    """ _ """
    diam = float(input()) * 2
    users = sorted(loads(input()))
    mincount = 0

    while users:
        mincount += 1
        users = list(filter(lambda x: x > diam + users[0], users))
    print(mincount)
main()
