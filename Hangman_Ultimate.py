import os
import random

def menu():
    os.system("cls || clear")
    print('Welcome to the Hangman game!')
    start = True
    while start:
        game(random_word())
        start == False
        play_again = input("Play Again? (Y/N) ").upper()
        if play_again == "Y":
            start = True
        else:
            print('Bye!')
            break
    


def game_level():
    # set amount of lives 

    print('Choose difficulty level: \n 1 - Easy \n 2 - Medium \n 3 - Hard')
    level_ok = False

    # set level of the game
    while level_ok == False:
        try:
            level = int(input('Enter number: '))
            if level == 1 or 2 or 3:
                if level == 1:
                    amount_of_lives = 10
                if level == 2:
                    amount_of_lives = 5
                if level == 3:
                    amount_of_lives = 3
                level_ok = True
                os.system("cls || clear")
            else:
                print('Enter valid diffuculty level!')
        except:
            print('Enter valid diffuculty level!')

    return amount_of_lives


def game(random_word):

    amount_of_lives = game_level()
    password = random_word[0]
    table = random_word[1]
    used_letters = []
    nickname = input('Enter your nickname: ')

        
    while amount_of_lives > 0:
        print('')
        print(nickname, ' has ', amount_of_lives, ' lifes left')
        lives(amount_of_lives)
        print('')
        print(' '.join(table))
        print(' ')

        # player choose the letter
        print('If you wanna quit game - write QUIT anytime!')
        print('Select a letter')
        letter = input().lower()
        os.system("cls || clear")
        if letter == 'quit':
            break
        else:
            if letter in used_letters:
                    print(letter + " was already used!")
                    amount_of_lives -= 1
            else:
                    # guess password
                if letter in password.lower():

                        # _ turn into guessed letter
                    for i in range(len(password)):
                        if(password[i].lower() == letter):
                            table[i] = password[i]
                    # check _ = amount of letters in the password
                    # check if the player has guessed the password        
                    if ''.join(map(str, table)) == password:
                        print('')
                        print(nickname, ' has ', amount_of_lives, ' lives left')
                        print('')
                        print(' '.join(table))
                        print(' ')
                        print(nickname, ' Victory!')
                        break
                    # when the player fails to guess
                else:
                    amount_of_lives -= 1

                used_letters.append(letter)

    if amount_of_lives < 1:
        print('Game Over')
        

def random_word():
    # open file 
    my_file = open('countries.txt', 'r', encoding = 'UTF-8' )
    
    # list of random passwords
    password_all = my_file.read()
    password_list = password_all.split('\n')

    # random password
    password = str(password_list[random.randint(0,len(password_list)-1)])
    table = list(password)
    #table -> show _ _ _ depending on amount of letters
    for i in range(len(password)):
        table[i] = '_'

    return password, table


def lives(amount_of_lives):
    # draw hearts depending on the number of lives
    lives = amount_of_lives
    for i in range(lives):
        i += 1
    print(i * ' ❤')


menu()


