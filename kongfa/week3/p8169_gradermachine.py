""" _ """
def main():
    """ _ """
    sss = int(input())
    eee = int(input())

    sumw = 0
    print("pass : ", end="")
    for i in range(sss, eee + 1):
        if i % 2 == 0:
            sumw += i
            print(i, end=" ")
    print("\nSum : " + str(sumw))

main()
