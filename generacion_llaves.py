import random

j=[0, 0, 1, 0, 0, 1, 0, 1, 1, 1]
p10=[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]


#se modifica el orden segun el p10 para poder crear la nueva lista p10(j)
#paso 1
p_10_j=[]

for i in p10:
    p_10_j.append(j[i-1])


ls_izq=[]
ls_der=[]
ps=[]

#almacenamos en unas listas cada mitad
#paso 2
ls_izq=p_10_j[:5]
ls_der=p_10_j[5:]
#Llamamos a una funcion aqui mismo para recorrer a la izquierda cada parte
ls_izq_2=[]
for i in range(len(ls_izq)):
    if i==(len(ls_izq)-1):
            ls_izq_2.append(ls_izq[0])
    else:
        ls_izq_2.append(ls_izq[i+1])

ls_der_2=[]
for i in range(len(ls_der)):
    if i==(len(ls_der)-1):
            ls_der_2.append(ls_der[0])
    else:
        ls_der_2.append(ls_der[i+1])
    
#unimos las 2 partes recorridas
#paso 3
ps=ls_izq_2+ls_der_2
ps_8=[]

#copiamos la llave con un ciclo para poder modificar una sin alterar la otra
for i in ps:
    ps_8.append(i)

#quitamos 2 bits para hacerla de 8 y usarla como llave
ps_8.pop(random.randint(0,(len(ps_8)-1)))
ps_8.pop(random.randint(0,(len(ps_8)-1)))

#guardamos en una funcion para poder llamar la llave desde otro código
def k1():
    return ps_8

#ahora repetiremos los pasos iguales para obtener la 2da llave
#paso 4
ls2_izq=ps[:5]
ls2_der=ps[5:]

#recorriendo 2 veces a la izquierda cada parte
ls2_izq_2=[]
ls2_der_2=[]

for i in range(len(ls2_izq)):
    if i==(len(ls2_izq)-2):
        ls2_izq_2.append(ls2_izq[0])
    elif i==(len(ls2_izq)-1):
        ls2_izq_2.append(ls2_izq[1])
    else:
        ls2_izq_2.append(ls2_izq[i+2])

for i in range(len(ls2_der)):
    if i==(len(ls2_der)-2):
        ls2_der_2.append(ls2_der[0])
    elif i==(len(ls2_der)-1):
        ls2_der_2.append(ls2_der[1])
    else:
        ls2_der_2.append(ls2_der[i+2])

ps2=ls2_izq_2+ls2_der_2
ps2_8=[]

#copiamos la llave 2 con un ciclo para modificar una sin alterar la otra
for i in ps2:
    ps2_8.append(i)

#quitamos 2 bits para hacerla de 8 y usarla como llave
ps2_8.pop(random.randint(0, (len(ps2_8)-1)))
ps2_8.pop(random.randint(0, (len(ps2_8)-1)))

def k2():
    return ps2_8