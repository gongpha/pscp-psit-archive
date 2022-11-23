""" _ """
def main():
    """ _ """
    coming = int(input())
    cost = int(input())
    per_head = int(input())
    we_come = int(input())
    print(per_head * ((we_come % coming) + (we_come // coming * cost)))

main()
