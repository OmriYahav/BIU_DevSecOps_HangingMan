from SentenceList import three_word_sentence_underscore
from SentenceList import three_word_sentence
from time import time_ns
import random

# Get random sentence index from "three_word_quotes" and use it to choose sentence in both of lists.
#three_word_sentence =--> "the real sentence" & three_word_sentence_underscore =--> "the blank sentence".
sentence_index = random.randint(0, len(three_word_sentence) - 1)
print("Wellcome to Hanging-Man Game , Have Fun \nGuess The Quote: --> ", three_word_sentence_underscore[sentence_index])

# Define variables : 1.total_score , 2.array for guessed letters , 3.current time as "game_start_time".
total_score = int()
guessed_letters = []
game_start_time = time_ns()


# Define  main function
def find_letter_in_words(letter):
    global total_score
    global guessed_letters

    # Check if the letter has already been guessed.
    if letter in guessed_letters:
        total_score -= 1
        print(f"You've already guessed this letter before.")
        print(f'"There is no more  " {letter.lower()} " is not in the quote , you loss 1 point.\nScore :{total_score}')
        print("Quote: --> ", three_word_sentence_underscore[sentence_index])
        return

    # Add the current letter to the guessed_letters list.
    guessed_letters.append(letter)

    # list to store all positions where the letter is found.
    positions = []

    # Iterate over each word in the sentence
    for word_index, word in enumerate(three_word_sentence[sentence_index]):

        # Iterate over each letter in the word.
        for letter_index, char in enumerate(word):

            # Check if the character matches the input letter.
            if char == letter:
                # Update the sentence with the letter at each position.
                blank_word_list = list(three_word_sentence_underscore[sentence_index][word_index])
                blank_word_list[letter_index] = letter
                three_word_sentence_underscore[sentence_index][word_index] = ''.join(blank_word_list)

                # Add 5 points to the user's score for every letter instance found.
                total_score += 5

                # Store the position where the letter is found in "positions array".
                positions.append((word_index, letter_index))

    # Print the updated sentence, inform the user about the letters found, and provide the updated score.
    if positions:
        print(
            f'Quote:-->{three_word_sentence_underscore[sentence_index]}\nLetters found in index:{positions}\nYou got more 5 points , keep trying!\nScore: {total_score}')


    # If a letter is not present in the word, the user's score will be dropped 1 point for each incorrect guess.
    else:
        total_score -= 1
        # Print the updated blank quote and inform the user about the incorrect guess and the updated score.
        print("Quote: --> ", three_word_sentence_underscore[sentence_index])
        print(f'" {letter.lower()} " is not in the sentence , you loss 1 point.\nScore :{total_score}')
    return positions


# Running the game until the user finishes guessing the quote.
while any('_' in word for word in three_word_sentence_underscore[sentence_index]):

    # Put Seperator and Take input from User.
    letter = input('-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - \nEnter a Letter:').lower()

    # Check if there is a input.
    if letter == '':
        print('No input! , please enter a letter to guess the sentence')

    # Check if user enter a number.
    elif letter.isnumeric():
        print('There is no numbers in The sentence , please enter a letter to guess The sentence')

    # Check if the user enter more then one letter.
    elif len(letter) > 1:
        print('There is more then one letter , only one letter is allowed')

    else:
        # Send the variable in lowercase to the function.
        find_letter_in_words(letter.lower())

# calculates the elapsed time since user start the game with nanoseconds.
# if elapsed time less than or equal to 30 seconds , the user get more 100 points.
if (time_ns() - game_start_time) // (1000000000) <= 30:
    total_score += 100
    print("Great! You have received a bonus of 100 points for completing the sentence in less than 30 seconds.")

# Print results: , Elapsed time , Completed sentence , Score .
print(f'\nElapsed time since you start the game : {(time_ns() - game_start_time) // (1000000000)} seconds')
print("Congratulations! You guessed the quote:", ' '.join(word for word in three_word_sentence[sentence_index]))
print(f'Your total score is : {total_score}')
