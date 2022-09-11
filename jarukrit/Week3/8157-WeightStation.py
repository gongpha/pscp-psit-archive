'''PSCP Program'''
def main() -> int:
    '''Leap year'''
    unbalance = False
    overweight = False
    avg_weight = float(input())
    point2, point3, point4 = float(input()), float(input()), float(input())
    point1 = (4 * avg_weight) - (point2 + point3 + point4)
    cond = avg_weight/2 >= point2 or avg_weight/2 >= point3
    cond2 = avg_weight/2 >= point1 or avg_weight/2 >= point4
    cond3 = (avg_weight/2+avg_weight) <= point2 or (avg_weight/2+avg_weight) <= point3
    cond4 = (avg_weight/2+avg_weight) <= point1 or (avg_weight/2+avg_weight) <= point4
    if cond or cond2 or cond3 or cond4:
        unbalance = True
    if (point1 + point2 + point3 + point4) > 15000:
        overweight = True

    if unbalance and overweight:
        print("Overweight")
    elif unbalance:
        print("Unbalance")
    elif overweight:
        print("Overweight")
    else:
        print("Pass %.2f" % point1)
    return 0
if __name__ == "__main__":
    main()
