import random

attempts = 8
welcome_message = 'H A N G M A N\n'
words_to_find = ['python', 'java', 'swift', 'javascript']
word_for_game = random.choice(words_to_find)
word_letters_as_set = set(word_for_game)
letters_already_found = []

word_all_covered = ''.join(['-' for letter in word_for_game])

# print(word_for_game)  # for debug purposes only: show the relevant word
# print(word_letters_as_set)  # for debug purposes only: show the letters in the word without duplicates.

print(welcome_message)
print(word_all_covered)

while attempts == 8:
    user_input = input('Input a letter: ')
    # print(attempts)  # for debug purposes only: show number of remaining attempts

    if user_input in word_letters_as_set:
        output_string = ''.join([letter if letter == user_input else '-' for letter in word_for_game])
        letters_already_found.append(user_input)
        # print(letters_already_found)  # for debug purposes only: show letters already found
        print(output_string)

    else:
        print("That letter doesn't appear in the word")
        print(word_all_covered)

    attempts -= 1

while attempts != 0:
    # print(f'{attempts}')  # for debug purposes only: show number of remaining attempts

    print(''.join([letter for letter in word_for_game if letter == letters_already_found]))
    user_input = input('Input a letter: ')

    if user_input in word_letters_as_set and user_input not in letters_already_found:
        output_string = [letter if letter == user_input or letter in letters_already_found
                         else '-' for letter in word_for_game]
        letters_already_found.append(user_input)
        # print(letters_already_found)  # for debug purposes only: show letters already found
        print(''.join(output_string))

    elif user_input in letters_already_found:
        output_string = [letter if letter == letter in letters_already_found
                         else '-' for letter in word_for_game]
        print(''.join(output_string))
        continue

    else:
        output_string = [letter if letter == letter in letters_already_found
                         else '-' for letter in word_for_game]
        print("That letter doesn't appear in the word")
        print(''.join(output_string))

    attempts -= 1

print('\nThanks for playing!')
