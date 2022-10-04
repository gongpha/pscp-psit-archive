""" _ """
def main():
    """ _ """
    weight = float(input())
    distribution = int(input())
    safe = float(input())
    shoot = 0
    curr_dist = 0
    while safe <= weight:
        weight /= distribution
        shoot += distribution ** curr_dist
        curr_dist += 1
    print(shoot)
main()
