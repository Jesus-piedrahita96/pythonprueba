def sacar_iva(subtotal):

    menu = """
        Iva a aplicar
        [1] exento del iva
        [2] Iva del 5%
        [3] Iva del 19%
        """
    iva = int(input(menu))

    if iva == 1:
        iva = 0
        return iva

    elif iva == 2:
        iva = (subtotal * 0.05)
        return iva

    elif iva == 3:
        iva = (subtotal * 0.19)
        return iva

    else:
        print ('dijite las opciones del menu')


def Calculo(productos):

    compras = []
    factura = []
    resumen_iva = []
    compra_total = float
    total = float
    separador = int

    for producto in range(productos):

        separador = 0
        print(f'producto #: {producto + 1}')
        codigo_producto = input('dijite el codigo: ')
        nombre_producto = input('dijite el nombre del producto: ')
        cantidad = int(input('cantidad: '))
        valor_unitario = int(input('valor unitario del producto: '))
        subtotal = valor_unitario * cantidad

        iva = sacar_iva(subtotal)
        resumen_iva.append(iva)
        total = subtotal + iva
        compras.append(total)
        separador += 1
        factura.extend([codigo_producto, nombre_producto, subtotal, total, separador])

    print('================ Impresion de Factura electronica ================')
    for i in factura:
        if i == 1:
            print('=====================================')
        
        if i != 1:
            print(i)

    compra_total = sum(compras)
    resumen_iva = sum(resumen_iva)

    print(f'total de venta {compra_total}')
    print(f'Iva de venta {resumen_iva}')
    

def main():
    productos = int(input('dijite la cantidad de productos a comprar por favor: '))
    Calculo(productos)


if __name__ == '__main__':
    main()