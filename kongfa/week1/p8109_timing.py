""" _ """
def main():
    """ _ """
    second = int(input())
    day = second//(24*60*60)
    second = second%(24*60*60)
    hour = second//(60*60)
    second = second%(60*60)
    minute = second//60
    second = second%60
    print(day, hour, minute, second)

main()
