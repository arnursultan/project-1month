import random

text = "Aidana" "Adilet"
words = text.split()
for a, word in enumerate(map(list, words)):
    random.shuffle(word)
    words[a] = ''.join(word)
print(*words)