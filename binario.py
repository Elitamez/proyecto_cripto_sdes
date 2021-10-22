#para obtener el archivo binario de la imagen
with open("vaca.png", "rb") as f:
    datos=f.read()
    print(type(datos))
    #convertir a lista ya que esta como "bytes"
    datos=list(datos)
    #print(datos)
#print(datos)

datos_binario=[]
#convertimos los numeros a binarios de 8 bits
for i in datos:
    datos_binario.append(format(i,'08b'))
print(datos_binario)

#cambiamos un byte para probar la encriptada
datos_binario[629]='00001100'
print(datos_binario)

#arreglo para convertir a decimal y así poder pasarlo a byte
for i in range(len(datos_binario)):
    #se cambian de binario a decimal, se coloca el 2 para que se sepa que estaba en formato binario
    datos_binario[i]=int(datos_binario[i],2)
print(datos_binario,"\n")

datos_binario=bytearray(datos_binario)
print(datos_binario,"\n")

with open("vaca_copia.png", "wb") as f:
    f.write(datos_binario)
    f.close()
    print("doc creado")

datos_binario=list(datos_binario)
for i in range(len(datos_binario)):
    datos_binario[i]=format(datos_binario[i],'08b')
print(datos_binario)

datos_binario[629]='00001010'
print(datos_binario)

for i in range(len(datos_binario)):
    #se cambian de binario a decimal, se coloca el 2 para que se sepa que estaba en formato binario
    datos_binario[i]=int(datos_binario[i],2)
print(datos_binario,"\n")

datos_binario=bytearray(datos_binario)
print(datos_binario,"\n")

with open("vaca_copia_2.png", "wb") as f:
    f.write(datos_binario)
    f.close()
    print("segunda parte creada")