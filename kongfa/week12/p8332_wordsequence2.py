""" _ """
def main():
    """ _ """
    raw1 = input()
    raw2 = input()
    print('\n'.join([raw2[:i] + raw1[i:] for i in range(max(len(raw1), len(raw2)) + 1)]))
main()
