'''PSCP Program'''
def main():
    '''Rock Paper Scissors'''
    instruc = input()
    a_point, b_point = 0, 0
    for i in range(0, len(instruc), 2):
        a_used = instruc[i:i+1]
        b_used = instruc[i+1:i+2]
        if a_used == 'R':
            if b_used == 'P':
                b_point += 1
            elif b_used == 'S':
                a_point += 1
        elif a_used == 'P':
            if b_used == 'R':
                a_point += 1
            elif b_used == 'S':
                b_point += 1
        elif a_used == 'S':
            temp = scissors(b_used)
            a_point += temp[0]
            b_point += temp[1]

    if a_point > b_point:
        print("A win ", a_point, "-", b_point, sep="")
    elif b_point > a_point:
        print("B win ", b_point, "-", a_point, sep="")
    else:
        print("DRAW", a_point)

def scissors(b_used):
    '''Scissors'''
    if b_used == 'R':
        return (0, 1)
    elif b_used == 'P':
        return (1, 0)
    return (0, 0)

if __name__ == "__main__":
    main()
