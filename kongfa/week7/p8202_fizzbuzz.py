""" _ """
def main():
    """ _ """
    nnn = int(input())
    for i in range(1, nnn + 1):
        mod_three = i % 3 == 0
        mod_five = i % 5 == 0
        if mod_three and mod_five:
            print("FizzBuzz")
        elif mod_three:
            print("Fizz")
        elif mod_five:
            print("Buzz")
        else:
            print(i)
main()
