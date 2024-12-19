def phonebook_merge(phonebook, second_phonebook):
    for name in second_phonebook:
        if name in phonebook:
            for phone in second_phonebook[name]:
                if phone not in phonebook[name]:
                    phonebook[name].append(phone)
        else:
            phonebook[name] = second_phonebook[name]