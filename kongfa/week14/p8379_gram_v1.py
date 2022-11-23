""" _ """
def main():
    """ _ """
    text = input()
    pairs = [
        text[i] + text[i + 1]
        for i in range(0, len(text)-1)
    ]
    mmm = max(pairs, key=pairs.count)
    print(mmm, pairs.count(mmm), sep='\n')
 
 
main()