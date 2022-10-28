""" _ """

# 0 = blocked/allocated
# 1 = free


def distribute(i, j, imap, countref, root):
    """ _ """

    if imap[i][j] != 1:
        return
    imap[i][j] = 0
    if i > 0:
        distribute(i-1, j, imap, countref, 0)
    if j > 0:
        distribute(i, j-1, imap, countref, 0)
    if i > 0 and j > 0:
        distribute(i-1, j-1, imap, countref, 0)
    if i < len(imap)-1:
        distribute(i+1, j, imap, countref, 0)
    if j < len(imap[0])-1:
        distribute(i, j+1, imap, countref, 0)
    if i < len(imap)-1 and j < len(imap[0])-1:
        distribute(i+1, j+1, imap, countref, 0)
    if i > 0 and j < len(imap[0])-1:
        distribute(i-1, j+1, imap, countref, 0)
    if i < len(imap)-1 and j > 0:
        distribute(i+1, j-1, imap, countref, 0)
    if root:
        countref[0] += 1
        return countref[0]


def main():
    """ _ """
    www, hhh = [int(x) for x in input().split()]
    iii = [
        [int(x) for x in input().split()] for _ in range(www)
    ]
    ref = [0]
    _ = [[distribute(i, j, iii, ref, 1) for j in range(hhh)] for i in range(www)]
    print(ref[0])
main()
