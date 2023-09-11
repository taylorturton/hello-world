text = input("Enter some text: ")
character_count = 0
consonant_count = 0
vowel_count = 0
letter_count = 0
word_count = 0

consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'

words = text.split()

for char in text:
    character_count += 1
    if char.lower() in consonants:
        consonant_count += 1
        letter_count += 1
    elif char.lower() in vowels:
        vowel_count += 1
        letter_count += 1

word_count = len(words)

print("Total characters: ", character_count)
print("Total letters: ", letter_count)
print("Total consonants: ", consonant_count)
print("Total vowels: ", vowel_count)
print("Total words: ", word_count)