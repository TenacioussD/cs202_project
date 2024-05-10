from collections import OrderedDict
def phonebook_lookup(filename):
   phonebook = dict()
   unwanted_chars = ".,- "
# open file, you may want to do some try and catch here
   with open("phonebook.txt",'r') as f:
     for line in f:
      #split each line into name and phone
      raw_words = line.split()
      #strip off the unwanted  charaters
      phonebook[raw_words[0].strip(unwanted_chars)] = raw_words[1].strip(unwanted_chars)
   return(phonebook)


print("\nPrinting your phonebook dict as key-value pair of name-phone")
print(phonebook_lookup("phonebook.txt"))
print("\nPrinting the length of your phonebook dict ")
print(len(phonebook_lookup("phonebook.txt")))

print("Allison-Neu updated phone number from :555-8200 to 555-8283")

# phonebook = dict()
phonebook_dict = phonebook_lookup("phonebook.txt")
# We can look up Allison-Neu in the phonebook dict,
for key in phonebook_dict:
    if key == "Allison-Neu":
        phonebook_dict[key] = '555-8283'  # and update her phone number.
    print(key, phonebook_dict[key])

print("\nPrinting dictionary methods and attributes...")
print(dir(phonebook_dict))
# phonebook_dict.update({"Allison-Neu": "555-8283"})

# using update method in dict
phonebook_dict.update({"Dr. Patrick": "555-666"})
print("\nPrinting Dr. Patricks phone number...")
print(phonebook_dict["Dr. Patrick"])

print("\n")

text = "Hello, I am trying to learn Python, however I am having difficulty"


def func_name(text):
    counts = dict()
    words = text.split()
    unwanted_chars = ".,-"
    for raw_word in words:
        word = raw_word.strip(unwanted_chars)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


word_counts = func_name(text)
print(word_counts)

# Create an OrderedDict
word_counts = OrderedDict(func_name(text))

# Print the OrderedDict
print(word_counts)
print("\n")


def func_name1(str):
    str = "Hello, hello, hello, hello, how are you?"
    count = {}
    unwanted_chars = ".,-"
    for raw_word in str.split():
        word = raw_word.strip(unwanted_chars)
        count[word] = count.get(word, 0) + 1
    return count


print(func_name1(str))
print("\n")

str = "1 2 3 4 5 5 4 3 2 1"


def func_name2(str):
    unwanted_chars = ".,-"
    count = {word.strip(unwanted_chars): str.split().count(word) for word in set(str.split())}
    return count


print(func_name2(str))
print("\n")

list_of_dicts = [{'Adam': 20}, {'Bob': 21}, {'Kate': 32, 'Dave': 18}]
list_of_dicts = {key: value for dict in list_of_dicts for key, value in dict.items()}
print(list_of_dicts)

course_code = ['CS201', 'CS202', 'CS203']
course_tutor = ['Adam', 'Ben', 'Sam']
new_dict = {course_code: course_tutor for course_code, course_tutor in zip(course_code, course_tutor)}
print(new_dict)

values: tuple = (1, 2, 4, "Geek")
print(values)

mytuple = ("Geeks",)
print(type(mytuple))

# NOT a tuple
mytuple = ("Geeks")
print(type(mytuple))