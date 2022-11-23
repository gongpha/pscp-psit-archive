"""(Last Docstring was a lie)"""
# NOTE: I WANT TO DO THIS PROBLEM USING RECURSION BUT SOME OF THE THE
#       TEST INPUTS ARE TOO BIG AND I HAVE NO ACCESS TO sys.setrecursionlimit().
#       SO IF YOU HAPPENS TO STUMBLE INTO THIS CODE AND WANT TO TRY IT FOR YOURSELF
#       JUST UNCOMMENTS THE LINES FROM THIS ONE!

# from sys import setrecursionlimit
# setrecursionlimit(10**6)
# def calculator_press(end: int, acc: int = 0) -> int:
#     """Return the amount of key presses it takes to
#        add up all the number from one up to the given parameter"""
#     if end == 0:
#         return acc
#     else:
#         return calculator_press(end-1, acc + len(str(end)) + 1)

def calculator_press(end: int) -> int:
    """Return the amount of key presses it takes to
       add up all the number from one up to the given parameter"""
    if end == 1:
        return 1
    else:
        output = 0
        for i in range(1, end+1):
            output += len(str(i)) + 1
        return output


if __name__ == "__main__":
    # input = int(input())
    # print(1 if input == 1 else calculator_press(input))

    print(calculator_press(int(input())))
