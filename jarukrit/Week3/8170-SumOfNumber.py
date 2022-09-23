'''PSCP Program'''
def main() -> int:
    '''SumOfNumber'''
    nums = []
    num1 = int(input())
    while True:
        temp = int(input())
        if temp == -1:
            break
        nums.append(temp)
        if sum(nums) == num1:
            break
    print(sum(nums))
if __name__ == "__main__":
    main()
