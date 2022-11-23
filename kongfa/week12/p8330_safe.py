""" _ """
def main():
    """ _ """
    correct = input()
    lock = input()
    count = 0
    for i, j in enumerate(correct):
        aidx = ord(j) - 65  # to alphabet index (A -> 0)
        encrypted = ord(lock[i]) - 65
        if aidx == encrypted:
            continue
        ten = encrypted
        rotd = 0
        while ten != aidx:
            ten = -1 if ten >= 25 else ten
            rotd += 1
            ten += 1
        rotu = 0
        while encrypted != aidx:
            encrypted = 26 if encrypted <= 0 else encrypted
            rotu += 1
            encrypted -= 1
        count += rotu if rotu <= rotd else (rotd if rotd < rotu else 0)
    print(count)
main()
