"""temperature """
def main():
    """main"""
    temp = float(input())
    txt1 = input()
    txt2 = input()
    if txt1 == "K":
        temp = temp-273.15
    elif txt1 == "F":
        temp = (temp-32)*(5/9)
    elif txt1 == "R":
        temp = temp*(5/9)-273.15
    if txt2 == "K":
        temp = temp+273.15
    elif txt2 == "F":
        temp = temp*(9/5)+32
    elif txt2 == "R":
        temp = (temp+273.15)*(9/5)
    print("%.2f" %temp)
main()
