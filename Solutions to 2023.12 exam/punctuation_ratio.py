def punctuation_ratio(text):
    withc = text.count(", and ")
    without = text.count(" and ") - withc

    if withc == 0 or without == 0:
        return 0
    else:
        return withc, without