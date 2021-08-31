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
    print(''' 
    ##############################################
                    JUEGO DEL AHORCADO
    ##############################################
    ''')
    choise()
    random_word = choise()
    print(random_word) # mostrar la palaba a adivinar
    linea = len(random_word)*"_"
    word = list(enumerate(random_word))
    linea = list(enumerate(linea))

    while linea != word:
        print(linea)
        letra = normalize(str(input("digite una letra: "))).upper()
        print(letra)
        
        if letra in random_word:          
            for num, character in word : #para los numero y caracteres en word
                if character == letra:  
                     linea[num] = word[num]
                     print( word )    
        os.system("cls")             
    
    print("gano")
                     
                     

                



 






if __name__ == "__main__":
    run()