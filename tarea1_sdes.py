import sboxes as sb

def main():
    ip_bits=[]
    
    #Almacenamos la ip del mensaje en una lista [paso ip(m)]
    for i in range(len(ip)):
        temp=ip.index(i+1)
        ip_bits.append(bits[temp])
    return ip_bits
    
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

def inicio_sboxes(xor):
    for i in range(len(xor)):
        xor[i]=str(xor[i])
    print(xor)
    
if __name__=="__main__":
    #Almacenamos las sboxes, la ip y las sk
    sb1=sb.sb1()
    sb2=sb.sb2()
    ip=sb.ip()
    sk1=sb.sk1()
    sk2=sb.sk2()
    
    #se coloca primero como String para que detecte en caso de existir "0" a la izquierda
    bits="0"
    while((len(bits))!=8):
        bits=input("Inserta los 8 bits: ")
        
    #Convertimos el String a una lista
    bits=list(bits)
    
    #Con este ciclo convertimos cada valor en entero
    for i in range(len(bits)):
        bits[i]=int(bits[i])
        
    print("\n\nTrabajaremos con las siguientes s-boxes y la siguiente IP")
    sbox_1()
    sbox_2()
    ip_normal()
    
    ip_m=main()
    print("\nIP(M)")
    print(ip_m,"\n")
    
    #obteniendo la E del procedimiento
    xor=inicio_xor(ip_m,sk1)
    print("xor\t",xor)
    
    inicio_sboxes(xor)