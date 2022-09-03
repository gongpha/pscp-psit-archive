"""PSCP"""
def main():
    """Jumping"""
    jumping()

def jumping():
    """Jumping"""
    for i in range(4):
        print_output(i+1)

def print_output(num):
    """Jumping"""
    for _ in range(3):
        print("Output%d"% int(num))

main()
