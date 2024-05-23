def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        words = ["".join([c for c in word if c not in ['!','?',':',',','.',')','(','"']]) for line in file for word in line.strip().split(" ")]
        freq = {w : words.count(w) for w in words if words.count(w) >= lower_limit}
        return(freq)

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))