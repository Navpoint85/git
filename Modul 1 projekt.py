"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiri Mastny
email: mastnyj@seznam.cz
"""

# Přihlašovací údaje
USERS = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Předpřipravené texty
TEXTS = [
"""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""",
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

if username in USERS and USERS[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu
try:
    text_index = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
    if text_index not in range(3):
        raise ValueError
except ValueError:
    print("Invalid selection, terminating the program..")
    exit()

selected_text = TEXTS[text_index]
words = [word.strip(",.:;!?") for word in selected_text.split()]

# Počítání slov
word_count = len(words)
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_words = sum(1 for word in words if word.islower() and word.isalpha())
numeric_strings = [int(word) for word in words if word.isdigit()]
numeric_sum = sum(numeric_strings)

# Výpis statistik
print("----------------------------------------")
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("----------------------------------------")

# Sloupcový graf
word_lengths = {}
for word in words:
    length = len(word)
    if length not in word_lengths:
        word_lengths[length] = 0
    word_lengths[length] += 1

print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
for length in sorted(word_lengths):
    print(f"{length: >3}|{'*' * word_lengths[length]: <13}|{word_lengths[length]}")