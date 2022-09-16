""" _ """
def main():
    """ _ """
    step = int(input())
    count = int(input())
    total_kao = 0
    total_step = 0
    step_height = 0
    for yyy in range(count):
        step_height = int(input())
        if step_height > step:
            print("NO")
            return
        total_kao += step_height
        if yyy == count - 1:
            if total_kao <= step:
                total_step += 1
            else:
                total_step += 2
        else:
            if total_kao > step:
                total_kao = step_height
                total_step += 1
            elif total_kao == step:
                total_kao = 0
                total_step += 1
    print(total_step)
main()
