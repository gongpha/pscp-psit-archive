"""PSCP Program"""
def main() -> int:
    """Boot Sequence"""
    out = []
    for i in range(int(input())):
        out.append(i+1)
    print(*out, sep="_")

if __name__ == "__main__":
    main()
