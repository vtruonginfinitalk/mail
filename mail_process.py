

import nagisa
from talon.signature.bruteforce import extract_signature

def detect_verb(input):
    texts = input.splitlines()
    flag = False
    for text in texts:
        words = nagisa.tagging(text)
        print("___________________________________")

        if '動詞' in words.postags:
            flag = True
            return flag
    return flag

def extract_mail(input):
    input = input.replace("=", "-")
    input = input.replace("*", "-")
    input = input.replace("_", "-")
    text, signature= extract_signature(input)
    print(type(signature))
    if type(signature) is str:
        print("Detected sig")
        print(signature)
    if type(signature) is str and detect_verb(signature) == True:
        print("Signature has V")
        return input
    return text