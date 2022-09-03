""" _ """
def main():
    """ _ """
    small = int(input())
    big = int(input()) * 5
    goal = int(input())
    if goal > big:
        left = goal - big
    else:
        left = goal - (goal // 5) * 5
    left -= small
    print(-1 if left > 0 else small + left)
main()
