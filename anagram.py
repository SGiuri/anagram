def find_anagrams(word, candidates):
    # working only with lower letters:
    word = word.lower()

    # creating a list in wich recording anagrams
    anagrams = []

    # trasforing  the word in a list of alphabetical ordered letters
    ordered_word = sorted(word)

    for candidate in candidates:

        # trasforing "candidate" in a list of alphabetical ordered lower letters
        sorted_candidate = sorted(candidate.lower())

        # if the word is not the candidate i check the lists
        if candidate.lower() != word:
            if sorted_candidate == ordered_word:
                anagrams.append(candidate)

    return anagrams
