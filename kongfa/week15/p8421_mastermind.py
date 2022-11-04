""" _ """

def main():
    """ _ """
    answ = input()
    guess = input()
    bbb = 0
    www = 0
    bbb += sum([answ[i] == guess[i] for i in range(4)])
    temp_ans = list(answ)
    for i in guess:
        if i in temp_ans:
            temp_ans.remove(i)
            www += 1
    www -= bbb
    print((
        'B' * bbb + 'W' * www
    ) + 'O' * (4 - (bbb + www)))


main()
