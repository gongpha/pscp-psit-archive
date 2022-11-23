""" _ """

def main():
    """ _ """
    ghosts = {
        'Banshee': "ace",
        'Demon': "bde",
        'Jinn': "adf",
        'Mare': "def",
        'Oni': "abd",
        'Phantom': "aef",
        'Poltergeist': "cdf",
        'Revenant': "abc",
        'Shade': "abf",
        'Spirit': "bcd",
        'Wraith': "cde",
        'Yurei': "bef",
    }

    devices = {
        'EMF Level 5': "a",
        'Ghost Writing': "b",
        'Fingerprints': "c",
        'Spirit Box': "d",
        'Freezing Temperatures': "e",
        'Ghost Orb': "f",
        'No evidence': ''
    }

    devicestr = []
    for device in [input(), input(), input()]:
        devicestr.append(devices[device])
    devicestr = ''.join(devicestr)

    ghostlist = list(ghosts.keys())

    for ghost in ghostlist.copy():
        for ccc in devicestr:
            if not ccc in ghosts[ghost]:
                if ghost in ghostlist:
                    ghostlist.remove(ghost)
    if len(ghostlist) == 0:
        print("Not yet discovered")
    else:
        print('\n'.join(ghostlist))




main()
