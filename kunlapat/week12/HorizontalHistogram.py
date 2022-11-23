"""fewgrhtfjyhg"""


import enum


def graph_fequency(str_input: str):
    str_sorted = sorted(sorted(str(set(str_input))), key=lambda i: i.islower())
    graph_raw = list(map(lambda letter: (lambda graph: [i for i in enum])(str(list("-"*str_sorted.count(letter)))), str_sorted))
    print()
    # return "\n".join(["{} : {}".format(letter, graph) for letter, graph in [(letter, graph)]])

if __name__ == "__main__":
    graph_fequency(input())