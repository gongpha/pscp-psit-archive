""" _ """
def main():
    """ _ """
    input() # unnecessary LMAO

    cccccc = [int(w) for w in input().split(' ')]
    ccc = []
    cccccc.sort()
    while len(cccccc):
        diff = 9999999999
        cccccccc = -1
        for i in range(len(cccccc)-1):
            ccccccc = cccccc[i + 1] -  cccccc[i]
            if diff > ccccccc:
                diff = ccccccc
                cccccccc = i
        ccc.append([cccccc[cccccccc], cccccc[cccccccc+1]])
        cccccc.remove(cccccc[cccccccc])
        cccccc.remove(cccccc[cccccccc])
    ccc.remove(ccc[-1])
    kosetyorsudtorsudpor = 0
    for cccc in ccc:
        ccc = cccc[1] - cccc[0]
        kosetyorsudtorsudpor += ccc
    print(kosetyorsudtorsudpor)
main()
