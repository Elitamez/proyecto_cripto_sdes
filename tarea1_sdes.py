import sboxes as sb

def main(m):
    ip_m=[]
    
    #Almacenamos la ip del mensaje en una lista [paso ip(m)]
    for i in ip:
        ip_m.append(m[i-1])
    return ip_m
    
#Función para mostrar la sbox 1
def sbox_1():
    print("\nSbox 1\n")
    for i in range (len(sb1)):
        for j in range(len(sb1)):
            print(sb1[i][j], end="\t")
        print()
    print("\n\n")
    
#Función para mostrar la sbox 2
def sbox_2():
    print("\nSbox 2\n")
    for i in range (len(sb2)):
        for j in range(len(sb2)):
            print(sb2[i][j], end="\t")
        print()
    print()

#Funcion para la IP
def ip_normal():
    print("\nIP\n\n",ip,"\n")
    
#Función para obtener obtener la E y realizar el xor con la sk
def inicio_xor(ip_m, sk):
    xor_e_sk=[]
    parteIzq=ip_m[:4]
    parteDer=ip_m[4:]
    
    #Alteramos la parte derecha para hacerla de 8 bits repitiendo los valores en orden inverso [paso E(R)]
    E=parteDer[::-1]+parteDer[::-1]
    
    #ciclo para realizar el xor
    for i in range(len(sk)):
        if (sk[i]==E[i]):
            xor_e_sk.append(0)
        else:
            xor_e_sk.append(1)
    return xor_e_sk

#iniciamos el proceso con las s-boxes
def inicio_sboxes(xor):
    #Convertimos los datos a str para poder realizar la comparación sin problema
    for i in range(len(xor)):
        xor[i]=str(xor[i])
    parteIzq=xor[:4]
    parteDer=xor[4:]
    
    #Crearemos nuevas listas con la primera fila y columna de las sboxes para hacer la comparación
    columna_s1=[]
    fila_s1=[]
    columna_s2=[]
    fila_s2=[]
    for i in range(4):
        columna_s1.append(sb1[i+1][0])
        fila_s1.append(sb1[0][i+1])
        columna_s2.append(sb2[i+1][0])
        fila_s2.append(sb2[0][i+1])
    
    #Ciclo para obtener el indice de la columna en la sbox lado izquierdo
    for i in columna_s1:
        if (parteIzq[0]==i[0]) and (parteIzq[3]==i[1]):
            x_izq=columna_s1.index(i)
    x_izq=x_izq+1
    #print(x_izq)

    #Ciclo para obtener el indice de la fila en la sbox lado izquierdo
    for i in fila_s1:
        if(parteIzq[1]==i[0]) and (parteIzq[2]==i[1]):
            y_izq=fila_s1.index(i)
    y_izq=y_izq+1
    #print(y_izq)
    
    #Ciclo para obtener el indice de la columna en la sbox lado derecho
    for i in columna_s2:
        if (parteDer[0]==i[0]) and (parteDer[3]==i[1]):
            x_der=columna_s2.index(i)
    x_der=x_der+1
    #print(x_der)
    
    #Ciclo para obtener el indice de la fila en la sbox lado derecho
    for i in fila_s2:
        if (parteDer[1]==i[0]) and (parteDer[2]==i[1]):
            y_der=fila_s2.index(i)
    y_der=y_der+1
    #print(y_der)

    #pasrte s0(l1) y s1(r1) del jamboard
    l_1=sb1[x_izq][y_izq]
    r_1=sb2[x_der][y_der]
    
    z=str(l_1+r_1)
    z=list(z)
    #print(z)
    
    #Comenzamos a aplicar el p4 a la z para después realizar el xor con el lado izquierdo
    z_p4=[]
    for i in p4:
        z_p4.append(z[i-1])
    return z_p4
    
def xor_final(z_p4, ip_m):
    #Separamos en 2 partes la ip del mensaje y creamos una nueva lista para almacenar el resultado del xor y tambien para almacenar la m'
    parteIzq=ip_m[:4]
    parteDer=ip_m[4:]
    xor_zp4_ipm=[]
    m_prima=[]
    
    #Convertimos los tipos de dato de la lista a entero para poder compararlo sin problema
    for i in range(len(z_p4)):
        z_p4[i]=int(z_p4[i])
    #print(z_p4)
    
    #realizamos el xor de la parte izquierda del mensaje con el p4(z)
    for i in range(len(z_p4)):
        if z_p4[i]==parteIzq[i]:
            xor_zp4_ipm.append(0)
        else:
            xor_zp4_ipm.append(1)
    
    #Agregamos la parte derecha de la m para completar los 8 bits
    m_prima=xor_zp4_ipm+parteDer
    return m_prima

def switch(m_prima):
    #Creamos la lista para almacenar el switch y lo dividimos en 2 partes para invertirlas
    sw_mprima=[]
    parte_1=m_prima[:4]
    parte_2=m_prima[4:]
    sw_mprima=parte_2+parte_1
    return sw_mprima   

def ip_inversa(m_prima_2, ip):
    #print("\t",ip)
    resultado=[]
    for i in range(len(ip)):
        temp=ip.index(i+1)
        resultado.append(m_prima_2[temp])
    return resultado
    
if __name__=="__main__":
    #Almacenamos las sboxes, la ip y las sk
    sb1=sb.sb1()
    sb2=sb.sb2()
    ip=sb.ip()
    sk1=sb.sk1()
    sk2=sb.sk2()
    p4=sb.p4()
    
    #se coloca primero como String para que detecte en caso de existir "0" a la izquierda
    m="0"
    while((len(m))!=8):
        m=input("Inserta los 8 bits del mensaje: ")
        
    #Convertimos el String a una lista
    m=list(m)
    
    #Con este ciclo convertimos cada valor en entero
    for i in range(len(m)):
        m[i]=int(m[i])
        
    print("\n\nTrabajaremos con las siguientes s-boxes y la siguiente IP")
    sbox_1()
    sbox_2()
    ip_normal()
    
    print("-----------------------------------------------------------------------")
    
    ip_m=main(m)
    print("\nIP(M)")
    print(ip_m,"\n")
    
    #obteniendo la E del procedimiento
    xor=inicio_xor(ip_m,sk1)
    print("xor\t",xor)
    
    #Obteniendo el p4(z)
    z_p4=inicio_sboxes(xor)
    print("\nP4(z)\t",z_p4,"\n")
    
    #Obteniendo m'
    m_prima=xor_final(z_p4,ip_m)
    print("m'\t", m_prima,"\n")
    
    #Obteniendo el sw(m')
    sw_mprima=switch(m_prima)
    print("Switch (m')\t", sw_mprima)
    
    #Obteniendo la E de la segunda parte
    xor2=inicio_xor(sw_mprima, sk2)
    print("\nxor2\t",xor2)
    
    #Obteniendo el p4(z) de la segunda parte
    z_p4_2=inicio_sboxes(xor2)
    print("\nP4(z2)\t",z_p4_2,"\n")
    
    #Obteniendo m' de la segunda parte
    m_prima_2=xor_final(z_p4_2, sw_mprima)
    print("m'2\t",m_prima_2,"\n")
    
    resultado=ip_inversa(m_prima_2, ip)
    print("IP_inversa(m'2)\t", resultado)