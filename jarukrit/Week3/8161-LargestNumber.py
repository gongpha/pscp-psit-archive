'''PSCP Program'''
def main() -> int:
    '''Largest Number'''
    num_in1, num_in2, num_in3 = input(), input(), input()
    num1 = int(num_in1 + num_in2 + num_in3)
    num2 = int(num_in1 + num_in3 + num_in2)
    num3 = int(num_in2 + num_in1 + num_in3)
    num4 = int(num_in2 + num_in3 + num_in1)
    num5 = int(num_in3 + num_in1 + num_in2)
    num6 = int(num_in3 + num_in2 + num_in1)
    one = highest_num(num1, num2, num3)
    two = highest_num(num4, num5, num6)
    if one > two:
        print(one)
    else:
        print(two)

def highest_num(num1: int, num2: int, num3: int) -> int:
    '''Returns the highest num from given parameters'''
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return num3

if __name__ == "__main__":
    main()
