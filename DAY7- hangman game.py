import random
import hangman_words
import hangman_art
print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_words.word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print("****************************<???>/"+str(lives)+ "LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess in display:
        print("you've already guessed "+guess)
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print("you guessed "+guess+", that's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
            print(f"it was "+chosen_word+"! ***********************YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(hangman_art.stages[lives])
