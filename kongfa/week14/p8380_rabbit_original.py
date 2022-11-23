""" _ """
 
def main():
    """ _ """
    rabbit = int(input())
    jump = int(input())
    carrot = int(input())
 
    rabbit_done = min(int((-1 + (1 + (8 * jump)) ** 0.5) // 2), carrot)
    rabbit_uwu = min(rabbit, rabbit_done)
    carrot_left = int(carrot - rabbit_uwu)
    jump_left = int(jump - (rabbit_uwu * (rabbit_uwu + 1)) // 2)
    rabbit_twt = max(0, int(rabbit - rabbit_uwu))
    print(*(
        ("Ahhahaha",) if (
            carrot_left == 0 and jump_left == 0 and rabbit_twt == 0
        ) else (rabbit_twt, jump_left, carrot_left)
    ))
main()