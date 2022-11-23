""" _ """
def main():
    """ _ """
    input()
    vote = int(input())
    scores = [int(input()) for _ in range(vote)]
    most = max(set(scores), key=scores.count)
    most_count = scores.count(most)
    print(most if most_count > vote / 2 else 0, most_count)
main()
