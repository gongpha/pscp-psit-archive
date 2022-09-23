""" _ """

def main():
    """ _ """
    initial = float(input())
    count = 0
    while initial >= 0.01:
        initial *= 3/5
        count += 1
    print(count - 1)
main()
