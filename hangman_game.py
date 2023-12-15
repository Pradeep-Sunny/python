import random
print("*******WELCOME TO HANGMAN GAME********")
words=["collage","class","bench","teacher","student","board","book"]
lifes=6
chosen_word=random.choice(words)
# print(chosen_word)

display=[]
for i in range(len(chosen_word)):
    display += '-'
print(display)

game_over=False
while not game_over:
    guessed_letter=input("guess a letter: ")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lifes -=1
        print("remaining lives "+str(lifes))
        if lifes==0:
            game_over=True
            print("you lose")
    if '-' not in display:
        game_over=True
        print("you win")
   
