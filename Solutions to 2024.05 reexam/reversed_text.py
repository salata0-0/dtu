def reversed_text(text, option):
    words = text.split()

    if option == "letters":
        reversed_words = []
        for word in words:
            reversed_word = ''.join(reversed(word))
            reversed_words.append(reversed_word)
        words = reversed_words
        
    elif option == "words":
        words.reverse()

    return ' '.join(words)