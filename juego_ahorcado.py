import random

def choise(): # funcion que nos ayuda a escoger una palabra de la lista 
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f :
            palabras.append(line)

    random_word = random.choice(palabras)
    random_word = random_word.upper()
    random_word = random_word[0:len(random_word)-1]
    #print(random_word) #escogemos una palabla random de la lista
    #print(len(random_word)) #lo largo de la palabra escogida
    return random_word

#def normalize(s):




def run():
    print(''' 
    ##############################################
                    JUEGO DEL AHORCADO
    ##############################################
    ''')
    choise()
    random_word = choise()
    print(random_word)
    a = len(random_word)
    b = a*"_ "
    print(b)
    letra = input("ponga una letra")
    letra = str(letra.upper)

    if letra in random_word:
        print("adivino una letra: ")




if __name__ == "__main__":
    run()