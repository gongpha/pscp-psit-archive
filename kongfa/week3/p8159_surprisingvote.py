""" _ """
def main():
    """ _ """
    total = float(input())
    best = float(input())
    left = total - best
    print(
        "Surprising" if abs(max(left - best, 0) - best) > 2 else
        "Not surprising"
    )
main()
