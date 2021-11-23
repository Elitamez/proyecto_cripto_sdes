#obtenemos el código binario de la imagen
#colocamos el nombre de la imagen que queremos usar y lo ejecutamos como lectura binaria
with open("imagen_encriptada.png", "rb") as f:
    #nos lo traera como lista de bytes
    datos=f.read()
    #print(datos)
    #lo convertimos a lista para poder manipularlo de forma más sencilla y esto mismo nos lo arroja cada parte como numero decimal
    datos_decimal=list(datos)
    #print(datos_decimal)

datos_binario=[]

#convertimos los numeros a binarios de 8 bits
for i in datos_decimal:
    datos_binario.append(format(i,'08b'))

#print(datos_binario)

def lista_binaria():
    return datos_binario