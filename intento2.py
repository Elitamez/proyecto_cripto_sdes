x=[0]
a=[]
for i in range (4):
    a.append(x*6)
print(a)

a[2][2]=15
print(str(len(a[1]))+"\n")

for i in range (len(a)):
    for j in range(len(a[1])):
        print(a[i][j],"\t", end=" ")
    print()

print()
print(str(a[2][2])[0])