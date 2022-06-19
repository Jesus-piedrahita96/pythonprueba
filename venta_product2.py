import pandas as pd


class VentaProductos:

  def __init__(self):
    self.__control_principal = True
    self.__control_iva = True
    self.__codigo_producto = []
    self.__nombre_producto = []
    self.__cantidad = []
    self.__valor_unitario = []
    self.__iva_lista = []
    self.__cont_producto = []
    self.__total_sin_iva = []
    self.__total_con_iva = []


  def __sacar_iva(self, subtotal):

    self.__menu = """
       \t ======= Iva a aplicar =======
        [1] exento del iva
        [2] Iva del 5%
        [3] Iva del 19%
        """

    self.__control_iva = True
    while self.__control_iva == True:

      self.__iva = int(input(self.__menu))

      if self.__iva == 1:
          self.__iva = 0
          self.__control_iva = False
          return self.__iva, self.__control_iva
          
      elif self.__iva == 2:
          self.__iva = (subtotal * 0.05)
          self.__control_iva = False
          return self.__iva, self.__control_iva

      elif self.__iva == 3:
          self.__iva = (subtotal * 0.19)
          self.__control_iva = False
          return self.__iva, self.__control_iva

      else:
          print ('dijite las opciones del menu')
  
  def __insertar_productos(self, cantidad):

    for posicion in range(cantidad):
      self.__contador = posicion
      print(f'Producto #: {self.__contador + 1}')
      self.__cod_pro = input('dijite el codigo: ')
      self.__nom_pro = input('dijite el nombre: ')
      self.__can = int(input('dijite la cantidad: '))
      self.__val_uni = int(input('dijite el valor: '))
      
      self.__sub_total = self.__val_uni * self.__can
      self.__total_sin_iva.append(self.__sub_total)
      self.__resumen_iva = self.__sacar_iva(self.__sub_total)
      self.__cont_producto.append(self.__contador)
      self.__iva_lista.append(self.__resumen_iva[0])
      self.__codigo_producto.append(self.__cod_pro)
      self.__nombre_producto.append(self.__nom_pro)
      self.__cantidad.append(self.__can)
      self.__valor_unitario.append(self.__val_uni)
      self.__total = self.__sub_total + self.__resumen_iva[0]
      self.__total_con_iva.append(self.__total)

  def __mostar_productos(self):
    
    self.__mostrar = {
      'Codigo' : self.__codigo_producto, 
      'Nombre' : self.__nombre_producto,
      'Cantidad': self.__cantidad,
      'Valor unitario' : self.__valor_unitario,
      'Total sin iva' : self.__total_sin_iva,
      'Valor de iva a incluir' : self.__iva_lista,
      'Total incluido iva' : self.__total_con_iva
      }

    self.df = pd.DataFrame(data= self.__mostrar)
    print(self.df)
    print('=' * 100)
    print(f'\f Total iva a incluir en la compra: {sum(self.__iva_lista)} \n Total de la compra sin iva: {sum(self.__total_sin_iva)} \n Total de la compra con iva: {sum(self.__total_con_iva)}')
      
  def __eliminar(self):

    self.__codigo_producto.clear()
    self.__nombre_producto.clear()
    self.__cantidad.clear()
    self.__valor_unitario.clear()
    self.__iva_lista.clear()
    self.__cont_producto.clear()
    self.__total_sin_iva.clear()
    self.__total_con_iva.clear()

  def main(self):
    
    menu = """
    =========== MENU PRINCIPAL =============
    \t Selecione la siguiente opcion:
      [1] comprar productos
      [2] ver la informacion de productos comprados
      [3] Eliminar informacion registrada
      [4] Salir
    """

    while self.__control_principal == True:
      opcion = int(input(menu))
      if opcion == 1:
        cantidad_productos = int(input('dijite la cantidad de productos a comprar: '))
        self.__insertar_productos(cantidad_productos)

      elif opcion == 2:
        self.__mostar_productos()

      elif opcion == 3:
        self.__eliminar()

      elif opcion == 4:
        self.__control_principal = False
        print('Gracias por utilizar mi sistema')
        return self.__control_principal

      else:
        print('Seleccione solo las opciones del menu... GRACIAS!')


if __name__ == '__main__':
  venta1 = VentaProductos()
  venta1.main()