""" _ """

def fff(phone, capa):
    """ _ """
    if phone == "iPhone 13 Pro":
        if capa == "128 GB":
            return "38900"
        elif capa == "256 GB":
            return "42900"
        elif capa == "512 GB":
            return "50900"
        elif capa == "1 TB":
            return "58900"
    return ggg(phone, capa)
def ggg(phone, capa):
    """ _ """
    if phone == "iPhone 13 Pro Max":
        if capa == "128 GB":
            return "42900"
        elif capa == "256 GB":
            return "46900"
        elif capa == "512 GB":
            return "54900"
        elif capa == "1 TB":
            return "62900"
    return ""
def main():
    """ _ """
    phone = input()
    capa = input()
    result = ""

    if phone == "iPhone 13 mini":
        if capa == "128 GB":
            result = "25900"
        elif capa == "256 GB":
            result = "29900"
        elif capa == "512 GB":
            result = "37900"
    elif phone == "iPhone 13":
        if capa == "128 GB":
            result = "29900"
        elif capa == "256 GB":
            result = "33900"
        elif capa == "512 GB":
            result = "41900"
    else:
        result = fff(phone, capa)
    print(result if len(result) else "Not Available")
main()
