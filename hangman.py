#Hangman!
#Hangman is a paper and pencil guessing game for two or more players.
#One player things of a word and the other tries to guess that word by suggesting letters and within a certain number of attempts

#There are 6 attempts to hangman and for each incorrect attempt a limb will be added to the hang man post.
#

#Steps to complete!


#The Hangman Board

def hangman(i):
    hangman_dict={0: '-------\n|\n|\n|\n|\n|\n------------', 
    1: '-------\n|     |\n|     O\n|\n|\n|\n------------',
    2: '-------\n|     |\n|     O\n|     |\n|\n|\n------------',
    3: '-------\n|     |\n|     O\n|   --|\n|\n|\n------------',
    4: '-------\n|     |\n|     O\n|   --|--\n|\n|\n------------',
    5: '-------\n|     |\n|     O\n|   --|--\n|    /\n|\n------------',
    6: '-------\n|     |\n|     O\n|   --|--\n|    / \ \n|\n------------'}
    return hangman_dict[i]

#Loop max turn count to 6.
#   In hangman there are 6 chances to guess the word.
tries = 0

#   Get input of the mystery word.


def get_word():
    mysteryword=''
    while mysteryword.isalpha()==False:
        mysteryword=input('Player 1 please input the mystery word: ')
        if mysteryword.isalpha()==False:
            print('Player 1 please input a valid mystery word!')
        elif mysteryword.isalpha()==True:
            return mysteryword.upper()

def player_guess():
    playerguess=''
    while playerguess.isalpha()==False:
        playerguess=input('Player 2 Please enter a letter or guess the word: ')
        if playerguess.isalpha()==True:
            return playerguess.upper()






print("Lets play hangman!!")
mysteryword=get_word()

def game(mysteryword):
    word_completion= '' *len(mysteryword)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6

    print(f'You have {tries} left')
    print(word_completion)
    print('\n')
   
    
    while not guessed and tries >0:
        playerguess=player_guess()
        if len(playerguess)==1:
            playerguess.append()



    





