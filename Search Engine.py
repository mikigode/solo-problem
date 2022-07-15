def search(x,y):
    return "Word found" if y in x else "Word not found"

text = input()
word = input()

print(search(text, word))
