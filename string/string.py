#Manipulation des String
first = "Terry"
last = "Vilver"
sentence = first + " [" + last + "] est un programmeur."
sentence2 = f"{first} [{last}] est un programmeur." #plus intuitif à lire et affiche la même chose que "sentence"

print("Test 1:")
print(f'{sentence}\n')
print("Test 2:")
print(f"{sentence2}\n")
print("Autre test:")
print(first[3:])
