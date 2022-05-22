def run():
    lista = [1, 4, 5, 6, 9, 13, 19, 21]
    for i in lista:
        if i % 2 != 0:
            continue
        print(i)

def run2():
    lista = [1, 4, 5, 6, 9, 13, 19, 21]
    comprehension = [i for i in lista if i%2 != 0]

    print(comprehension)
    
    
def num_filter():
    lista = [1, 4, 5, 6, 9, 13, 19, 21]
    numimpar = list(filter(lambda x: x%2 != 0, lista))
    print(f'numeros impar: {numimpar}')
    numpar = list(filter(lambda x: x%2 == 0, lista))
    print(f'numeros par: {numpar}')



def num_map():
    lista = [1, 2, 3, 4, 5]
    lista_potencializada = [i**2 for i in lista]
    #print(lista_potencializada)
    num_filter = list(filter(lambda x: x**2, lista))
    num_mapa = list(map(lambda x: x**2, lista))
    print(f'se utilizo la funcion filter: {num_filter}')
    print(f'se utilizo la funcion map: {num_mapa}')

    
def num_reduce():
    from functools import reduce

    lista = [2, 2, 2, 2, 2]
    num = 1
    for i in lista:
        num = num * i
    
    print(f'resultado utilizando el bucle for: {num}')

    reducir = reduce(lambda x, y: x*y, lista)
    print(f'resultado utilizando la funcion reduce: {reducir}')

def cambiar_nombre():
    cadena = 'stefany'
    nombre_nuevo = cadena.replace("s","p")
    print(nombre_nuevo)

if __name__ == '__main__':
    #num_reduce()
    cambiar_nombre()