def word_frequency(paragraph: list) -> dict:
    frequency = {}
    text = " ".join(paragraph).lower()
    words = text.split()

    for word in words:
        word = word.strip("!#$%&()*+, -./:;<=>?@[]^_`{|}~")

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


"""
import string

def word_frequency(paragraph: list) -> dict:
    frequency = {}
    text = " ".join(paragraph).lower()
    words = text.translate(str.maketrans('', '', string.punctuation)).split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
"""