import random

programming_languages = 'python java javascript swift'.split()
programming_language = random.choice(programming_languages)
letters_in_language = set(programming_language)
number_of_attempts = 8
letters_already_found = []
games_won = 0
games_lost = 0
game_headline = 'H A N G M A N\n'

print(game_headline)

while True:

    gamestart = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if gamestart == 'play':

        while number_of_attempts > 0:

            if letters_in_language == set(letters_already_found):
                print(f'You guessed the word {programming_language}!\n\nYou survived!')
                games_won += 1
                letters_already_found = []
                break

            else:
                print('')
                masked_word = [letter if letter in letters_already_found else '-' for letter in programming_language]
                print(''.join(masked_word))
                user_input = input('Input a letter: ')

                if len(user_input) != 1:
                    print(f'Please, input a single letter.')

                elif not user_input.isalpha() or user_input == '' or not user_input.islower():
                    print('Please, enter a lowercase letter from the English alphabet.')

                elif user_input in letters_in_language and user_input not in letters_already_found:
                    letters_already_found.append(user_input)

                elif user_input in letters_in_language and user_input in letters_already_found:
                    number_of_attempts -= 1
                    print(f"You've already guessed this letter.")

                elif user_input not in letters_in_language:
                    number_of_attempts -= 1
                    print("That letter doesn't appear in the word.")

        else:
            print('')
            masked_word = [letter if letter in letters_already_found else '-' for letter in programming_language]
            print(''.join(masked_word))
            print('You lost!')
            games_lost += 1
            continue

    if gamestart == 'exit':
        quit()

    if gamestart == 'results':

        print(f'You won: {games_won} times.\nYou lost: {games_lost} times.')
        continue
