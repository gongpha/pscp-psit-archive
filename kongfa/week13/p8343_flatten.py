""" _ """
import json
def recur(item, newlst):
    """ _ """
    if isinstance(item, list):
        for i in item:
            recur(i, newlst)
    else:
        newlst.append(item)
def main():
    """ _ """
    lst = input()
    lst = json.loads(lst)
    newlst = []
    for i in lst:
        recur(i, newlst)

    newlst.sort(reverse=True)
    print(newlst)

main()
