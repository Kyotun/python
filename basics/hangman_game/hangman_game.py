#Hangman game
import random
import hangman_words
import hangman_art

lives = 6
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
control_list = ['_'] * len(chosen_word)

print(hangman_art.logo)
print("Welcome to the Hangman game!")

while not end_of_game:
 guessed_letter = input("Please guess a letter: ").lower()

 #Check guessed letter
 for index in range (len(chosen_word)):
  if chosen_word[index] == guessed_letter:
   control_list[index] = guessed_letter
 
 #If there is no matched characters life -= 1
 if guessed_letter not in chosen_word:
  lives -= 1

 print(f"Life: {lives}")
 print(f"{control_list}")
 print(hangman_art.hangman_pics[lives])

 #No life left. Game is over!
 if lives == 0:
  end_of_game = True
  print("Sorry but you lost :(.")

 #User guessed every char correct. Game is over, user has won!
 if '_' not in control_list:
  end_of_game = True
  print("Congratulations. You won!")


