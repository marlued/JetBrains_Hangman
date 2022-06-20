import random

programming_languages = 'python java javascript swift'.split()
programming_language = random.choice(programming_languages)
letters_in_language = set(programming_language)
number_of_attempts = 8
letters_already_found = []
game_headline = 'H A N G M A N\n'

print(game_headline)

while number_of_attempts > 0:
    number_of_attempts -= 1
    masked_word = [letter if letter in letters_already_found else '-' for letter in programming_language]
    print(''.join(masked_word))
    user_input = input('Input a letter: ')

    if user_input in letters_in_language and user_input in letters_already_found:
        continue

    elif user_input in letters_in_language:
        letters_already_found.append(user_input)

    elif user_input not in letters_in_language:
        print("That letter doesn't appear in the word.")

print('\nThanks for playing!')
