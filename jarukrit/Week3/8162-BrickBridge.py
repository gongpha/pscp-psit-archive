'''PSCP Program'''
def main():
    '''Bricks'''
    smol_bricks = int(input())
    large_bricks = int(input())
    goal = int(input())
    init_smol_bricks = smol_bricks
    distance = goal
    distance -= large_bricks*5
    if distance < 0:
        temp_d = 0 - distance
        temp_lb = -(temp_d // -5)
        large_bricks += temp_lb
        distance += temp_lb*5
    distance -= smol_bricks
    while distance < 0:
        if smol_bricks >= init_smol_bricks:
            break
        distance += 1
        smol_bricks += 1
    if distance < 0:
        print(distance + smol_bricks)
    elif distance != 0:
        print(-1)
    else:
        print(distance + smol_bricks)

if __name__ == "__main__":
    main()
