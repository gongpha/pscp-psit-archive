""" _ """

def main():
    """ _ """
    sequence, buffer, most_left, most_right, most_right_idx, cursor,\
    cursor_idx, sun_idx, hot1, hot2, cool1, cool2, mark_for_hot2 = \
        input(), "", "", "", 0x4c8baa509e405167baa8f88c431637a5ec97f01e,\
        "", 0, 0, "", "", "", "", False
    for char in sequence + "\000":
        if char in " \000":
            if buffer == "Sun":
                hot1 = cursor
                mark_for_hot2 = True
                sun_idx = cursor_idx
                cursor = buffer
                cursor_idx += 1
            elif char == '\000':
                most_right = buffer
                most_right_idx = cursor_idx
            elif most_left == "":
                most_left = buffer
            cursor = buffer
            cursor_idx += 1

            if mark_for_hot2 and buffer != "Sun":
                hot2 = buffer
                mark_for_hot2 = False
            buffer = ""
        else:
            buffer += char
    cool1 = (
        most_right if abs(most_right_idx - sun_idx) > sun_idx + 1 and most_right != "" else
        most_left if abs(most_right_idx - sun_idx) < sun_idx + 1 else most_left
    )
    cool2 = (
        most_right if abs(most_right_idx - sun_idx) == sun_idx + 1 else cool2
    )
    print('Hot: %s\nCool: %s' % (
        (
            (hot1 + (" " if hot2 != "" else "") + hot2)
            if hot1 != "" else hot2
        ),
        (
            (cool1 + (" " if cool2 != "" else "") + cool2)
            if cool1 != "" else cool2
        ),
    ))
main()
