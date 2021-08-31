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
    print(title)
    cont = 0
    choise()
    random_word = choise()
    print(random_word) # mostrar la palaba a adivinar
    linea = len(random_word)*"_"
    word = list(enumerate(random_word))
    linea = list(enumerate(linea))

    while linea != word:
        cont += 1        
        print(graphics[cont])
        print(linea)
        letra = normalize(str(input("digite una letra: "))).upper()
        
        if letra in random_word:          
            for num, character in word : #para los numero y caracteres en word
                if character == letra:  
                     linea[num] = word[num]

                     print( word )    
        os.system("cls")             
    
    print("gano")
                     
                     

                



 






if __name__ == "__main__":
    run()