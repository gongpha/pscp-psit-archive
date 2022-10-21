""" Hate RecursionError ? Just reduce them ! """

def fibo(arr):
    """ _ """
    if arr[0] == 0:
        return arr[1]
    if arr[3] >= 980:
        arr[4] = True
        return arr[1]
    arr[0], arr[1], arr[2], arr[3] = arr[0] - 1, arr[2], arr[1] + arr[2], arr[3] + 1
    rrr = fibo(arr)
    if arr[4]:
        arr[3] -= 1
        if arr[3] == 0:
            return fibo(arr)
    return rrr

def main():
    """ _ """
    print(fibo([int(input()), 0, 1, 0, False]))

main()
