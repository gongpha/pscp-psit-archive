""" _ """
def main():
    """ _ """
    turn_on = False
    state = 0
    warm = 0
    prev = -0x58db2fb880ba44b5d212c5147bbb6ccb940171bc # i would like to avoid -INF
    while True:
        iii = input()
        if iii == "End":
            break
        iii = float(iii)

        state = (
            state if turn_on else (
                0 if iii - prev > 6 else
                1 - state
            )
        )
        turn_on = not turn_on
        if turn_on and state == 1:
            warm += 1
        prev = iii

    print(warm)
main()
