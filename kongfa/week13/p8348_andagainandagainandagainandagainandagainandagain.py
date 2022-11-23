""" _ """

def main():
    """ _ """
    text = input()
    textlist = text.split(' ')

    newlist = []
    for i in textlist:
        counter = 0
        newstring = ""
        for j in i:
            if not j.isalpha():
                continue
            if j in "aeiouAEIOU":
                counter += 1
            newstring += j
        if counter >= 2:
            newlist.append(newstring)

    newlist.sort()
    if len(newlist) == 0:
        print("Nope")
    else:
        for i in newlist:
            print(i)

main()
