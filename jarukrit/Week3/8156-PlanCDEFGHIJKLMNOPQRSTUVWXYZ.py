'''PSCP Program'''
def main() -> int:
    '''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
    direction = input()
    print(order_num(float(input()), float(input()), float(input()), direction))
    return 0

def order_num(num1: float, num2: float, num3: float, direction: str) -> str:
    '''Order numbers'''
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if direction == "Descend":
        return "%.2f, %.2f, %.2f"% (num3, num2, num1)
    elif direction == "Ascend":
        return "%.2f, %.2f, %.2f"% (num1, num2, num3)

if __name__ == "__main__":
    main()
