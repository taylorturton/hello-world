text = input("Enter some text: ")
character_count = 0
consonant_count = 0
vowel_count = 0
letter_count = 0

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'

for char in text:
    character_count += 1
    if char.lower() in consonants:
        consonant_count += 1
        letter_count += 1
    elif char.lower() in vowels:
        vowel_count += 1
        letter_count += 1

print("Total characters: ", character_count)
print("Total letters: ", letter_count)
print("Total consonants: ", consonant_count)
print("Total vowels: ", vowel_count)