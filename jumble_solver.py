from itertools import permutations
from spellchecker import SpellChecker

jumble = input("Enter the jumble: ")
temp_list = list(permutations(jumble))

spell = SpellChecker()
print(*spell.known(list(map("".join, temp_list))))
