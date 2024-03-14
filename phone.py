def phonebook_lookup(filename):
    phonebook_dict = dict()
    unwanted_chars = ".,- "
      with open(filename,'r') as f:
            for line in f:
raw_words = line.split()   phonebook_dict[raw_words[0].strip(unwanted_chars)] = raw_words[1].strip(unwanted_chars)
      return(phonebook_dict)
phonebook=phonebook_lookup("phonebook.txt")