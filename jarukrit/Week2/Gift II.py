"""Prints something to console"""
def main() -> int:
    """The main function"""
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    odd_even(int(input()))
    return 0

def odd_even(num):
    '''Find Even'''
    if num%2 == 0:
        print(num)
if __name__ == "__main__":
    main()
