#Hangman!
#Hangman is a paper and pencil guessing game for two or more players.
#   One player things of a word and the other tries to guess that word by suggesting letters and within a certain number of attempts.
#   There are 6 attempts to hangman and for each incorrect attempt a limb will be added to the hang man post.
#   Steps to complete!
#   The Hangman Board
def hangman(i):
    hangman_dict={6: '-------\n|\n|\n|\n|\n|\n------------', 
    5: '-------\n|     |\n|     O\n|\n|\n|\n------------',
    4: '-------\n|     |\n|     O\n|     |\n|\n|\n------------',
    3: '-------\n|     |\n|     O\n|   --|\n|\n|\n------------',
    2: '-------\n|     |\n|     O\n|   --|--\n|\n|\n------------',
    1: '-------\n|     |\n|     O\n|   --|--\n|    /\n|\n------------',
    0: '-------\n|     |\n|     O\n|   --|--\n|    / \ \n|\n------------'}
    return hangman_dict[i]

#   Get input of the mystery word.
def mystery_word():
    mysteryword=''
    while mysteryword.isalpha()==False:
        mysteryword=input('Player 1 please input the mystery word: ')
        if mysteryword.isalpha()==False:
            print('Player 1 please input a valid mystery word!')
        if mysteryword.isalpha()==True:
            return mysteryword.upper()

#   Get input of the player guess.
def player_guess():
    playerguess=''
    while playerguess.isalpha()==False:
        playerguess=input('Player 2 Please enter a letter or guess the word: ')
        if playerguess.isalpha()==False:
            print('Player 1 please input a valid mystery word!')
        if playerguess.isalpha()==True:
            return playerguess.upper()

#   Game functionality.
def game():

    play=True   
    #   In hangman there are 6 chances to guess the word.
    tries=6
    hiddenword=[]
    guessedletters=[]
    guessedwords=[]
    mw=mystery_word()

    for i in range(len(mw)):
        hiddenword.append('_')

    while play==True and tries>0: 
        print(hiddenword)
        pg=player_guess()

        #   Check if the player guessed a letter.
        if len(pg)==1:

            #   Check if the player already guessed the letter.
            if pg in guessedletters:
                print('You have already guessed this letter, please try again. \n')

            #   If the player guessed letter is WRONG (NOT in the mystery word.) 
            elif pg not in mw:
                tries -=1
                print(f'Your guess of {pg} is wrong.')
                guessedletters.append(pg)
                #   Print out the hangman visual representation to signify a wrong guess. (Add a limb to the hangman.)
                print(hangman(tries))
                
                #   If tries reaches 0
                if tries == 0:
                    print("Game Over, You have no more tires left.\n")
                    print(f'The hidden word was {mw} \n')

            #   The player guessed a correct letter that is in the mystery word.
            elif pg in mw:
                print(f'Your guess of {pg} is correct. ')
                guessedletters.append(pg)

                #   We are using list comprehension to 
                index_pos=[i for i,letter in enumerate(mw) if letter==pg]
                for index in index_pos:
                    hiddenword[index]=pg
                
                #   If the player guesses all the letters inside the mysterword they win.
                if ''.join(hiddenword) == mw:
                    play=False
                    print("Congratulations, You have guessed the correct word! You win!\n")

        #   Creating the conditions if the player guessed an entire word
        elif len(pg) == len(mw):
            if pg in guessedwords:
                print('You have already guessed this word, please try again. \n')

            #   If the player guessed word is WRONG. (NOT the mystery word.) 
            elif pg != mw:
                tries -=1
                print(f'Your guess of {pg} is wrong. \n')
                guessedwords.append(pg)
                #   Print out the hangman visual representation. (Add a limb to the hangman.)
                print(hangman(tries))

                #   If tries reaches 0
                if tries == 0:
                    print("Game Over, You have no more tries left.\n")
                    print(f'The hidden word was {mw} \n')

            # The player guessed the correct word 
            elif pg == mw:
                print(f'Your guess of {pg} is correct. ')
                guessedwords.append(pg)
                play=False
                print(f'Congratulations ! {mw} is the mystery word! You win!!\n')
     
        else:
            print('Your guess is incorrect. Please try again. \n')
            tries -=1
            print(hangman(tries))

# Ask the players if they want to keep on playing
def main():
    keep_playing=True
    while keep_playing==True:
        game()
        play=input('Would you like to keep playing? (Y/N): ')
        if play=='y' or play =='Y':
            keep_playing= True
        else:
            print('Game Over! Thankyou for playing!')
            keep_playing= False

if __name__ == "__main__":
    main()    






    





