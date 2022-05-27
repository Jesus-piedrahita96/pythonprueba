cant_pro=int(input("cuantos productos vas a comprar: "))
cant_pro=0
for i in range(cant_pro):
    codi=int(input("codigo producto: "))
    nom=input("nombre producto: ")
    cant=float(input("cantidad a comprar: "))
    uni=float(input("valor unitario: "))
    val_pro = cant * uni
    tipo_iva =int(input("tipo de iva a aplicar"))
    
    
    if tipo_iva ==1:
        iva=val_pro*0
    elif tipo_iva ==2:
        iva=val_pro * (5 / 100)
    else: 
        tipo_iva ==3
        iva=val_pro * (19 / 100)  
               
    val_final=val_pro + iva
    
    valortotalcompra1= cant_pro + val_pro
    
    val_totaltotal=valortotalcompra1 + val_final

print(codi)
print(nom)
print(val_pro)
print(val_final)
# print(valortotalcompra1)
print(val_totaltotal)