""" Nightmare version (3 STATEMENTS and No loop statement) """
def main():
    """ _ """
    duration = int(input())
    desired = int(input())
    print(
        (
            165 * (duration // 2 - duration // 6) + (duration // 6)
        ) if 165 * (duration // 2 - duration // 6) + (duration // 6) <= desired else (
            ((desired // 331) * 331) +
            (
                0 if ((desired // 331) * 331) >= desired else
                165 if ((desired // 331) * 331) + 165 >= desired else
                330 if ((desired // 331) * 331) + 330 >= desired else 331
            ) +
            ((12 * (
                duration - (
                    ((desired // 331) * 331) // 331 * 6 + (
                        1 if ((desired // 331) * 331) >= desired else
                        3 if ((desired // 331) * 331) + 165 >= desired else
                        5 if ((desired // 331) * 331) + 330 >= desired else 6
                    )
                )
            )) if (
                duration - (
                    ((desired // 331) * 331) // 331 * 6 + (
                        1 if ((desired // 331) * 331) >= desired else
                        3 if ((desired // 331) * 331) + 165 >= desired else
                        5 if ((desired // 331) * 331) + 330 >= desired else 6
                    )
                )
            ) > 0 else 0)
        )
    )
main()














# another zero-loop version
#
# def main():
#     """ _ """
#     duration = int(input())
#     desired = int(input())
#     mudtotal = 165 * (duration // 2 - duration // 6) + (duration // 6)
#     if mudtotal <= desired:
#         print(mudtotal)
#         return
#     total = (desired // 331) * 331 # 331 = 165 + 165 + 1 (6 (3) secs)
#     total_sec = total // 331 * 6
#     total_sec += (
#         1 if total       >= desired else
#         3 if total + 165 >= desired else
#         5 if total + 330 >= desired else 6
#     )
#     total += (
#         0   if total       >= desired else
#         165 if total + 165 >= desired else
#         330 if total + 330 >= desired else 331
#     )
#     sec_left = duration - total_sec
#     total += (12 * (sec_left )) if sec_left > 0 else 0
#     print(total)
#
###########################################################################
# regular loop version
# def main():
#     """ _ """
#     duration = int(input())
#     desired = int(input())
#     sec = 2
#     mud = 0
#     mudtotal = 165 * (duration // 2 - duration // 6) + (duration // 6)
#     if mudtotal <= desired:
#         print(mudtotal)
#         return
#     while sec - 1 < duration:
#         ins = mud < desired
#         mud += (
#             1 + (164 * int(sec % 6 != 0))
#             if ins else (1 + duration - sec) * 12
#         )
#         if not ins:
#             break
#         sec += 2
#     print(mud)
