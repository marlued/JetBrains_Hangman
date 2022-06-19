import random

attempts = 8
welcome_message = f'H A N G M A N # {attempts} attempts'
words_to_find = ['python', 'java', 'swift', 'javascript']
word_for_game = random.choice(words_to_find)
word_letters_as_set = set(word_for_game)

word_all_covered = ''.join(['-' for letter in word_for_game])

print(word_for_game)  # for debug purposes only: show the relevant word
print(word_letters_as_set)  # for debug purposes only: show the letters in the word without duplicates.

print(welcome_message)
print(word_all_covered)

while attempts != 0:
    strings_for_output = []
    user_input = input('Input a letter: ')
    print(attempts)  # for debug purposes only: show number of remaining attempts

    if user_input in word_letters_as_set:
        output_string = ''.join([letter if letter == user_input else '-' for letter in word_for_game])
        print(output_string)

    else:
        print('NO')

    attempts -= 1


