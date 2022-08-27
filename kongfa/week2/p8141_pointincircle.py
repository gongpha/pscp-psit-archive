""" _ """

import math

def main():
    """ _ """
    xxx = float(input())
    yyy = float(input())
    radius = float(input())
    xnn = float(input())
    ynn = float(input())

    distance = math.sqrt((xxx - xnn)**2 + (yyy - ynn)**2)

    print(distance <= radius)
main()
