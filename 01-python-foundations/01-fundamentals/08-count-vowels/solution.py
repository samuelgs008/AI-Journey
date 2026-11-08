# 08 - Count Vowels
letters = input().lower().replace(" ", "")
vowel_count = 0
for letter in letters:
    vowel_count += letter in "aeiou"
consonant_count = len(letters) - vowel_count
print(f"VOWELS = {vowel_count}")
print(f"CONSONANTS = {consonant_count}")
