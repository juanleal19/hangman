import random
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
    random_word = normalize(random_word).upper()
    #random_word = random_word[0:len(random_word)-1]
    #print(random_word) #escogemos una palabla random de la lista
    #print(len(random_word)) #lo largo de la palabra escogida
    return random_word

def lineas():
    palabra = choise()
    palabra = len(palabra)
    palabra = palabra*"_ "
    print(palabra)


def run():
    print(''' 
    ##############################################
                    JUEGO DEL AHORCADO
    ##############################################
    ''')
    choise()
    random_word = choise()
    print(random_word) # mostrar la palaba a adivinar
    lineas()

    while True:
        letra = normalize(str(input("digite una letra: "))).upper()
        print(letra)
        if letra in random_word:
            print("adivino una letra")
        else:
            print("letra incorrecta")




if __name__ == "__main__":
    run()