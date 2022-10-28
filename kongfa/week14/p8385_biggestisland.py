""" _ """

# 0 = blocked/allocated
# 1 = free


def distribute(i, j, imap, count, root):
    """ _ """

    if imap[i][j] != 1:
        return
    imap[i][j] = 0

    if root:
        arr = [0]
        count.append(arr)
        count = arr
    count[0] += 1

    if i > 0:
        distribute(i-1, j, imap, count, 0)
    if j > 0:
        distribute(i, j-1, imap, count, 0)
    if i > 0 and j > 0:
        distribute(i-1, j-1, imap, count, 0)
    if i < len(imap)-1:
        distribute(i+1, j, imap, count, 0)
    if j < len(imap[0])-1:
        distribute(i, j+1, imap, count, 0)
    if i < len(imap)-1 and j < len(imap[0])-1:
        distribute(i+1, j+1, imap, count, 0)
    if i > 0 and j < len(imap[0])-1:
        distribute(i-1, j+1, imap, count, 0)
    if i < len(imap)-1 and j > 0:
        distribute(i+1, j-1, imap, count, 0)


def main():
    """ _ """
    www, hhh = [int(x) for x in input().split()]
    iii = [
        [int(x) for x in input().split()] for _ in range(www)
    ]
    islands = []
    _ = [[distribute(i, j, iii, islands, 1) for j in range(hhh)] for i in range(www)]
    print(sorted(islands, key=lambda x: x[0], reverse=True)[0][0])
main()
