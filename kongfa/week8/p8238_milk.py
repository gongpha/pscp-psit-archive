""" _ """
def main():
    """ _ """
    each = int(input())
    jar_quota = int(input())
    free = int(input())
    money = int(input())

    jar = money // each
    jarcap = jar

    while jar_quota > 0 and jarcap >= jar_quota:
        more = (jarcap // jar_quota) * free
        jarcap = jarcap % jar_quota
        jar += more
        jarcap += more
    print(jar)
main()
