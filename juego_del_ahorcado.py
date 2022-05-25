import random

def aleatorio(palabra):
    palabra = random.choice(palabra)
    return palabra


def read():
    palabras = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        for palabra in f:
            palabras.append(palabra)

    seleccion = aleatorio(palabras)
    return seleccion

def lista(palabras):
    lis = []
    for palabra in palabras:
        lis.append(palabra)
    return lis


def run():
    print('Adivina la palabra 💤')
    seleccion = read()
    seleccion = seleccion.replace("\n", "")

    tamaño =  []
    tamaño = ["-"]*len(seleccion)
    tamaño_sin_espacio = "".join(tamaño)
    while tamaño != seleccion:
        print(tamaño_sin_espacio)
        letras = input("dijite una letra por favor: ")
        for i in seleccion:
            if i == letras:
                seleccion = lista(seleccion)
                key = []

        


if __name__ == '__main__':
    run()