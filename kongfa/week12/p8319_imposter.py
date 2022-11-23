""" _ """
import json
def main():
    """ _ """
    players = {}
    dead = {}
    alive = {}
    started = False

    while True:
        line = input()
        if line == "Start":
            started = True
        elif line == "End":
            break
        else:
            if started:
                dead.update({line : players[line]})
            else:
                players.update(json.loads(line))
    for kkk, _ in players.items():
        if kkk not in dead:
            alive.update({kkk : players[kkk]})
    print(
        str(sum([1 for ppp in alive if players[ppp] == "Impostor"])) +
        " Impostor Remains\n***Alive***" + '\n' * (len(alive) > 0) +
        "\n".join([
            "%s : %s" % (kkk, vvv)
            for kkk, vvv in sorted(alive.items(), key=lambda item: item[0])
        ]) +
        "\n***Dead***" + '\n' * (len(dead) > 0) +
        "\n".join([
            "%s : %s" % (kkk, vvv)
            for kkk, vvv in sorted(dead.items(), key=lambda item: item[0])
        ])
    )
main()
