'''PSCP Program'''
def main() -> int:
    '''Stepper II'''
    var_n = int(input())
    var_m = int(input())
    step = 1
    if var_n > var_m:
        var_m -= 2
        step = -1
    for i in range(var_n-1, var_m, step):
        print(i+1)
    return 0

if __name__ == "__main__":
    main()
