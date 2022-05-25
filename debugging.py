def proceso(num):
    num_list = []
    for i in range(1, num+1):
        if num % i == 0:
            num_list.append(i)

    return num_list


def validation(num):
    try:
        if num < 0:
            raise ValueError('No se pueden ingresar numeros negativos')
        else:
            return proceso(num)
    except ValueError as ve:
        print(ve)
 
        
def run():
    try:
        numero = int(input('dijite un numero: '))
        print(validation(numero))
        print('finalizo el programa')
    except ValueError:
        print('No puedes ingresar letras o caacteres especiales')


if __name__ == '__main__':
    run()