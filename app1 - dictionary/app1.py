import json

def find_word(dictionary, word):
    if word in dictionary:
        return "\n".join(dictionary[word])
    else:
        return "Word not found"

with open("data.json") as data:
    content = json.load(data)
    word = input("Enter the word you want to know")
    print(find_word(content,word))