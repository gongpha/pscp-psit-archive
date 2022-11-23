""" _ """
def main():
    """ _ """
    temp = float(input())
    if temp >= 36 and temp < 38:
        print('No Fever')
    elif temp >= 38 and temp < 39:
        print('Mild Fever')
    elif temp >= 39 and temp < 40:
        print('High Fever')
    else:
        print('Very High Fever')
main()
