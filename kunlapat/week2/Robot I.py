"""Converts seconds into a timestamp"""


def main() -> int:
    """The main function"""
    name = str(input())
    age = float(input())
    
    if age < 18:
        print(f"{name}, you can pass.")
    else: 
        print(f"{name}, you shall not pass.")
        

    return 0

if __name__ == "__main__":
    main()
