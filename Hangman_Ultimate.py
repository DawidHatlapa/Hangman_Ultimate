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
    # ustawia liczbę żyć

    print('Choose difficulty level: \n 1 - Easy \n 2 - Medium \n 3 - Hard')
    level_ok = False

    # ustawia poziom gry - liczbę żyć,
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

        # gracz wybiera literę
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
                    # odgadnięcie hasła
                if letter in password.lower():

                        # _ zamienia się w odgadniętą literę
                    for i in range(len(password)):
                        if(password[i].lower() == letter):
                            table[i] = password[i]
                    # sprawdza czy ilość _ = ilości liter w haśle
                    # sprawdza czy graczowi udało się odgadnąć hasło            
                    if ''.join(map(str, table)) == password:
                        print('')
                        print(nickname, ' has ', amount_of_lives, ' lives left')
                        print('')
                        print(' '.join(table))
                        print(' ')
                        print(nickname, ' Victory!')
                        break
                    # gdy gracz nie odgadnie
                else:
                    amount_of_lives -= 1

                used_letters.append(letter)

    if amount_of_lives < 1:
        print('Game Over')
        

def random_word():
    # otwiera plik 
    my_file = open('countries.txt', 'r', encoding = 'UTF-8' )
    
    # lista losowanych haseł
    password_all = my_file.read()
    password_list = password_all.split('\n')

    #funkcja losująca hasło 
    password = str(password_list[random.randint(0,len(password_list)-1)])
    table = list(password)
    #table -> powoduje wyświetlenie się _ _ _ w zależności od ilości liter danego hasła
    for i in range(len(password)):
        table[i] = '_'

    return password, table


def lives(amount_of_lives):
    # rysuje serca w zależności od ilości żyć
    lives = amount_of_lives
    for i in range(lives):
        i += 1
    print(i * ' ❤')


menu()


