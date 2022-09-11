'''PSCP Program'''
def main() -> int:
    '''Triangle'''
    side1, side2, side3 = float(input()), float(input()), float(input())
    highest = highest_num(side1, side2, side3)
    cond1 = highest[0]**2 == highest[1]**2 + highest[2]**2
    cond2 = abs((highest[0]**2) - (highest[1]**2 + highest[2]**2)) <= 0.01
    if cond1 or cond2:
        print("Yes")
    else:
        print("No")

def highest_num(num1: float, num2: float, num3: float) -> float:
    '''Returns the highest num from given parameters'''
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return num3, num2, num1

if __name__ == "__main__":
    main()
