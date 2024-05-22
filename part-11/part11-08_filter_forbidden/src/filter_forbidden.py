def filter_forbidden(string: str, forbidden: str):
    strList = [n for n in string if n not in forbidden]
    return "".join(strList)

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)