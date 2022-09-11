'''PSCP Program'''
def main() -> int:
    '''GraderMachine'''

    from_num, to_num, step = int(input()), int(input()), int(input())
    for i in range(from_num, to_num, step):
        print(i)

if __name__ == "__main__":
    main()
