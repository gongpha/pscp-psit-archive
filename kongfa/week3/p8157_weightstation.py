""" _ """
 
def is_unbalance(www, aaa) -> bool:
    """ _ """
    return abs(www - aaa) > aaa / 2
 
def main():
    """ _ """
    average = float(input())
    www2 = float(input())
    www3 = float(input())
    www4 = float(input())
    www1 = (average * 4) - (www2 + www3 + www4)
 
    if www1 + www2 + www3 + www4 > 15000:
        print("Overweight")
        return
 
    if is_unbalance(www1, average) or is_unbalance(www2, average)\
        or is_unbalance(www3, average) or is_unbalance(www4, average):
        print("Unbalance")
        return
 
    print("Pass %.2f" % www1)
 
main()