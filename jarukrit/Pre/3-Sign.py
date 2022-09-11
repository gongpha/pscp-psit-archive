'''Test'''
from math import ceil
def main():
    '''Also test'''
    length = "*"*int(input())
    height = int(input())
    for i in range(ceil(height/2)-1):
        temp = []
        temp.append(" "*((ceil(height/2)-1)-i))
        temp.append(length)
        print(*temp, sep="")
    for i in range((height//2)+1):
        temp = []
        temp.append(" "*i)
        temp.append(length)
        print(*temp, sep="")

main()
