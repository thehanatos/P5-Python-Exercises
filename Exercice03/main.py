words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyels = ["a", "e", "i", "o", "u", "y"]
voyel_number = 0
words_with_voyels = []


def count_voyels(word):
    voyel_number = 0
    for voyel in word:
        if voyel in voyels:
            voyel_number += 1
    return word, voyel_number


for word in words:
    words_with_voyels.append((count_voyels(word)))

print(words_with_voyels)
