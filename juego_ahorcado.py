import os
import random

from os import system, name

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
title = (''' 
    ##############################################
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                      
    ##############################################
    ''')

graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
WIN = ('''
$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\       $$\ $$\ $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |      $$ |$$ |$$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |      $$ |$$ |$$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |      $$ |$$ |$$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |      \__|\__|\__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |                  
    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |      $$\ $$\ $$\ 
    \__|     \______/  \______/       \__/     \__|\______|\__|  \__|      \__|\__|\__|
                                                                                       
                                                                                      
''')

LOST = ('''
 __      __   ______   __    __        __         ______    ______   ________              ___ 
/  \    /  | /      \ /  |  /  |      /  |       /      \  /      \ /        |            /   |
$$  \  /$$/ /$$$$$$  |$$ |  $$ |      $$ |      /$$$$$$  |/$$$$$$  |$$$$$$$$/        __  /$$$/ 
 $$  \/$$/  $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$ \__$$/    $$ |         /  |/$$ /  
  $$  $$/   $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$      \    $$ |         $$/ $$ |   
   $$$$/    $$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ | $$$$$$  |   $$ |          __ $$ |   
    $$ |    $$ \__$$ |$$ \__$$ |      $$ |_____ $$ \__$$ |/  \__$$ |   $$ |         /  |$$  \_ 
    $$ |    $$    $$/ $$    $$/       $$       |$$    $$/ $$    $$/    $$ |         $$/  $$   |
    $$/      $$$$$$/   $$$$$$/        $$$$$$$$/  $$$$$$/   $$$$$$/     $$/                $$$/ 
                                                                                               
''')

def choise(): # funcion que nos ayuda a escoger una palabra de la lista 
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f :
            palabras.append(line)

    random_word = random.choice(palabras)
    random_word = normalize(random_word).upper().replace(" ","")
    random_word = random_word[0:len(random_word)-1]
 
    return random_word

def run():
    try:
        print(title)
        cont = 0
        lives = 8
        random_word = choise()
        print(random_word) # mostrar la palaba a adivinar
        linea = len(random_word)*"_"
        word = list(enumerate(random_word))
        linea = list(enumerate(linea))

        while linea != word:       
            print(graphics[cont])
            print(linea, "\n Do you have: "+str(lives) +" lives", cont)
            letra = normalize(str(input("digite una letra: "))).upper()
            
            if letra in random_word:          
                for num, character in word : #para los numero y caracteres en word
                    if character == letra:  
                        linea[num] = word[num]
                        
                os.system("cls")  
            else:
                cont += 1
                lives -= 1
                os.system("cls")      

            if cont == 7:
                os.system("cls") 
                print(LOST) 
                break
            elif linea == word:
                print(WIN)
        play= int(input("press 1 if you want to play again "))
        
        if play == 1:
            run()
        else:
            os.system("cls")
            print("bye")

    except ValueError:
        print("you can only enter letters")
        


if __name__ == "__main__":
    run()