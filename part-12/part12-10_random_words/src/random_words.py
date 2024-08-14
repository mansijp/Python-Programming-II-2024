from random import randint

def word_generator(characters: str, length: int, amount: int):
    return ("".join(characters [randint(0, length)] for i in range(length)) for j in range(amount))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)