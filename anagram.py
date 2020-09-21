def find_anagrams(word, candidates):
    selected = []
    for candidate in candidates:
        if candidate == word:
            break

    for candidate in candidates:
        if ordered_letters(candidate) == ordered_letters(word):
            selected.append(candidate)

    return selected


def ordered_letters(word):
    new_word = ""
    for letter in set(word):
        new_word += letter * word.count(letter)

    return new_word.lower()
