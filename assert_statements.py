def proceso(num):
    #assert (num < 0), "No se pueden ingresar numeros negativos"
    num_list = []
    for i in range(1, num+1):
        if num % i == 0:
            num_list.append(i)

    return num_list
 
        
def run():

    numero = input('dijite un numero: ')
    assert numero.isnumeric(), "No puedes ingresar letras o caracteres especiales, tampoco numeros negativos"
    print(proceso(int(numero)))
    print('finalizo el programa')


if __name__ == '__main__':
    run()