"""eiosagdnfzvclkbnl"""
import json


def main() -> int:
    crewmate_list = {}
    prompt = input()
    while prompt != "Start":
        crewmate_list.append(*json.loads(prompt))
        prompt = input()

    print(crewmate_list)
    return 0

if __name__ == "__main__":
    main()