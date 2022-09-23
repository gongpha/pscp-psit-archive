""" _ """

def scanline(line):
    """ _ """
    if not line.startswith('Reply from'):
        return -1
    time = line[line.find('time') + 4:line.find('ms')]
    if time[0] == '<':
        return 0
    elif time[0] == '=':
        return int(time[1:])

def main():
    """ _ """
    _, _, lll3 = input(), input(), input()
    ppp1, ppp2, ppp3, ppp4 = input(), input(), input(), input()

    if lll3.find('[') == -1 and lll3.find(']') == -1:
        # pure ip
        ip_address = lll3[8:lll3.find('with') - 1]
    else:
        ip_address = lll3[lll3.find("[") +1 :lll3.find("]")]

    qqq1 = scanline(ppp1)
    qqq2 = scanline(ppp2)
    qqq3 = scanline(ppp3)
    qqq4 = scanline(ppp4)

    success = (
        int(qqq1 >= 0) +
        int(qqq2 >= 0) +
        int(qqq3 >= 0) +
        int(qqq4 >= 0)
    )

    print("Ping statistics for " + ip_address + ":")
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%d%% loss)," % (
        success, 4 - success, int((1 - success / 4) * 100)
    ))
    if success > 0:
        # amen
        minvvv = min(
            0x3ddea12693509b09790dfc64b9e78efadb780cc6 if qqq1 == -1 else qqq1,
            0xc083cd7e00d83f171cf159d8523735218e3df97e if qqq2 == -1 else qqq2,
            0x9a1e3c83ccb94f65311b9f08d2f0abcf6b92e444 if qqq3 == -1 else qqq3,
            0xc48d37d72bc7dc4aa2c702bc1232a32ade52effc if qqq4 == -1 else qqq4
        )
        maxvvv = max(
            -0xfa0b863358510385ddefe6992c8fa7fe7d5f347f if qqq1 == -1 else qqq1,
            -0x840315ad4a3b9120e02917f580f4e055055c8469 if qqq2 == -1 else qqq2,
            -0x7942ae6908db7200dab8a87041fbc240b4c5799b if qqq3 == -1 else qqq3,
            -0x2973b36a517a3b1d07d1b4f674b6ca39979c1cc8 if qqq4 == -1 else qqq4
        )

        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" % (
            minvvv,
            maxvvv,
            int(-(-(
                (0 if qqq1 == -1 else qqq1) +
                (0 if qqq2 == -1 else qqq2) +
                (0 if qqq3 == -1 else qqq3) +
                (0 if qqq4 == -1 else qqq4)
            ) / success))
        ))
main()
