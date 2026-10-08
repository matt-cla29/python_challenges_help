import random
import random_words
found_letters = 0
random_word = random_words.words(random_words)
user_guess = input("guess your first letter of the word:")
while found_letters < len(random_word):
    if user_guess in random_word:
        print("you have found one of the letters in the word!")
    else:
        print("that letter is not in the word, try again")
        user_guess = input("guess another letter: ")
        continue
       
if found_letters == len(random_word):
    print("all the letters have been found correctly, now guess the word!")
    user_word_guess = input("guess the word: ")
    if user_word_guess == random_word:
        print("you have guess the word correctly!, well done!")