""" _ """

def main():
    """ _ """
    basics = (
        'what', 'why', 'where', 'when', 'how', 'the', 'who', 'which', 'that', 'this'
    )
    text = input()
    while True:
        buffer = ""
        for ccc in text:
            if not ccc.isalpha():
                buffer += ccc
                continue
            begin = ord('A' if ccc.isupper() else 'a')
            buffer += chr((ord(ccc) - begin + 1) % 26 + begin)

        bbb = ''.join([i for i in buffer if i.isalpha() or i == ' ']).split()
        for www in bbb:
            if www.lower() in basics:
                print(buffer)
                return
        text = buffer
main()
