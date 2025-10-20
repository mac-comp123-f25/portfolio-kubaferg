def count_words(word, long_text):
    words = long_text.split()
    return words.count(word)
print(count_words("ban", "ban banana ban banana",))
