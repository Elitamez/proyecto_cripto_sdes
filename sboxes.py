import generacion_llaves as gl

sbox=[0]
s1=[]
s2=[]
p_4=[]

#orden en el que se alterará el mensaje original
ip_1=[2, 6, 3, 1, 4, 8, 5, 7]

sk_1=gl.k1()
sk_2=gl.k2()

#orden en el que se repetiran los bits de la parte derecha del ip(m)
E_1=[4, 1, 2, 3, 2, 3, 4, 1]

#formando las matrices
for i in range (5):
    s1.append(sbox*5)
    s2.append(sbox*5)
    
#Definiendo el orden del p4
p_4=[2, 4, 3 , 1]

#Llenando la sbox 1 (izquierda)
s1[0][0]="S1"
s1[0][1]="00"
s1[0][2]="01"
s1[0][3]="10"
s1[0][4]="11"

s1[1][0]="00"
s1[2][0]="01"
s1[3][0]="10"
s1[4][0]="11"

s1[1][1]="01"
s1[1][2]="00"
s1[1][3]="11"
s1[1][4]="10"

s1[2][1]="11"
s1[2][2]="10"
s1[2][3]="01"
s1[2][4]="00"

s1[3][1]="00"
s1[3][2]="10"
s1[3][3]="01"
s1[3][4]="11"

s1[4][1]="00"
s1[4][2]="01"
s1[4][3]="11"
s1[4][4]="10"

#Llenando la sbox 2
s2[0][0]="S2"
s2[0][1]="00"
s2[0][2]="01"
s2[0][3]="10"
s2[0][4]="11"

s2[1][0]="00"
s2[2][0]="01"
s2[3][0]="10"
s2[4][0]="11"

s2[1][1]="00"
s2[1][2]="01"
s2[1][3]="10"
s2[1][4]="11"

s2[2][1]="10"
s2[2][2]="00"
s2[2][3]="01"
s2[2][4]="11"

s2[3][1]="11"
s2[3][2]="00"
s2[3][3]="01"
s2[3][4]="10"

s2[4][1]="10"
s2[4][2]="01"
s2[4][3]="00"
s2[4][4]="11"
     
def sb1():
    return s1

def sb2():
    return s2

def p4():
    return p_4

def ip():
    return ip_1

def sk1():
    return sk_1

def sk2():
    return sk_2

def E():
    return E_1