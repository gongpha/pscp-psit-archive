""" _ """
def main():
    """ _ """
    summation = 0
    num = input()
    for i in num:
        summation += int(i)

    last = int(num[-3:]) * 10
    total = summation + last

    if total > 9999:
        total = str(total)[-4:]
    elif total < 1000:
        total += 1000
    print(total)
main()
