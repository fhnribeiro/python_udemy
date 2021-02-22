import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

def find_word(word):
    word = word.lower()
    if word in dictionary:
        return [1, "\n".join(dictionary[word])]
    elif word.title() in dictionary:
        return [1, "\n".join(dictionary[word.title()])]
    else:
        closest = get_close_matches(word, dictionary.keys(),1,0.8)
        if len(closest) > 0:
            return [2, closest[0]]
        else:    
            return [0, "Word not found"]

code = 0
while code != 1:
    word = input("Enter the word you want to know: ")
    [code, result] = find_word(word)
    if(code == 2):
        confirm = input("Did yoy mean %s? Type Y for yes and N for no: " % result)
        if(confirm.lower() == "n"):
            code = 0
        else:
            [code, result] = find_word(result)
    if code == 1:
        print(result)