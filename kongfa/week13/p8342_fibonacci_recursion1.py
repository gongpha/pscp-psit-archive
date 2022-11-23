""" _ """

def fibo(num):
    """ _ """
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)

def main():
    """ _ """
    print(fibo(int(input())))

main()
