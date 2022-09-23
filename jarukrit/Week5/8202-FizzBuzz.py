'''PSCP Program'''
def main():
    '''Fizz Buzz Pre'''
    for i in range(1, int(input())+1):
        mul_three = i % 3 == 0
        mul_five = i % 5 == 0
        if mul_three and mul_five:
            print("FizzBuzz")
        elif mul_three:
            print("Fizz")
        elif mul_five:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()
