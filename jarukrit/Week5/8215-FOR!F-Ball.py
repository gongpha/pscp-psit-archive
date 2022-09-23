'''PSCP Program'''
def main():
    '''FOR!F-Ball'''
    instruc = input()
    cup_1, cup_2, cup_3 = True, False, False
    for i in instruc:
        if i == "A":
            cup_1, cup_2 = cup_2, cup_1
        elif i == "B":
            cup_2, cup_3 = cup_3, cup_2
        elif i == "C":
            cup_1, cup_3 = cup_3, cup_1
    if cup_1:
        print(1)
    elif cup_2:
        print(2)
    elif cup_3:
        print(3)

if __name__ == "__main__":
    main()
