j=[0, 0, 1, 0, 0, 1, 0, 1, 1, 1]
p10=[3, 5, 2, 7, 4, 10, 1, 9, 8, 6]


#se modifica el orden segun el p10 para poder crear la nueva lista p10(j)
p_10_j=[]

for i in p10:
    p_10_j.append(j[i-1])


ls_izq=[]
ls_der=[]
ps=[]

#almacenamos en unas listas cada mitad
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
ps=ls_izq_2+ls_der_2

#quitamos 2 bits para hacerla de 8 y usarla como llave (en este caso decidimos quitar los primeros 2)
ps=ps[2:]

#guardamos en una funcion para poder llamar la llave desde otro código
def k1():
    return ps