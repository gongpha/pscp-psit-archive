""" _ """
def main():
    """ _ """
    num = int(input())
    ans = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            ans = ans + i
    print(ans)
main()
