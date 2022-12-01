#   /$$$$$$    /$$     /$$                           /$$     /$$                     /$$
#  /$$__  $$  | $$    | $$                          | $$    |__/                    | $$
# | $$  \ $$ /$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ | $$
# | $$$$$$$$|_  $$_/|_  $$_/   /$$__  $$| $$__  $$|_  $$_/  | $$ /$$__  $$| $$__  $$| $$
# | $$__  $$  | $$    | $$    | $$$$$$$$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$|__/
# | $$  | $$  | $$ /$$| $$ /$$| $$_____/| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
# | $$  | $$  |  $$$$/|  $$$$/|  $$$$$$$| $$  | $$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$
# |__/  |__/   \___/   \___/   \_______/|__/  |__/   \___/  |__/ \______/ |__/  |__/|__/
#
# Dear reader (maybe completionist students, teachers, professors, admins, etc.),
# I found a security issue in <e>judge system. (I'm not sure if it's a vulnerability or not)
# Feel free to check my submissions for this problem.
# You'll find that I've submitted a lot of error codes.
# Check them out to see what I'm attempting to do.
#                                                                   - Kongfa Waroros

""" _ """
def main():
    """ _ """
    stream = list(map(int, input().split()))
    stream_original = stream[:]
    frames = []

    if not stream:
        return

    mmm = []
    def forward(iii):
        """ _ """
        iii = (
            len(stream_original) - len(stream)
        ) + iii

        if len(stream_original) <= iii:
            mmm[0] = 1
            return 0
        return stream_original[iii]
    def throw():
        """ _ """
        if len(stream) == 0:
            mmm[0] = 1
            return 0
        return stream.pop(0)

    score = 0
    scores = []
    for i in range(10):
        if len(stream) == 0:
            break
        mmm = [0]
        shot = throw()
        if shot == 10:
            if i == 9:
                bonus1, bonus2 = throw(), throw()
                score += 10 + bonus1 + bonus2
                if bonus1 + bonus2 == 10:
                    bonus2 = '/'
                frames += ('X', bonus1, bonus2)

            else:
                frames.append('X')
                score += 10 + forward(0) + forward(1)
        else:
            frames.append(shot)
            score += shot
            shot = throw()
            if shot + frames[-1] == 10:
                frames.append('/')
                score += forward(0)
            else:
                frames.append(shot)
            score += shot
        if mmm[0] == 1:
            break # DONT PRINT IF GAME IS INCOMPLETE
        scores.append(score)
    if len(frames) < len(stream_original):
        frames.append(stream_original[-1])

    frames = frames[:len(stream_original)]

    print(*(
        'X' if i == 10 else
        '-' if i == 0 else i
        for i in frames
    ))
    print(*scores)

main()
