mi_tupla = (1,2,3,4)
t = (5,5.5,'f')
print(type(mi_tupla))
print(mi_tupla[2])
print(mi_tupla[-1])
mi_tupla_2 = (1,2,(10,20),3)
print(mi_tupla_2[2])
print(mi_tupla_2[2][1])
t1=(1,2,3)
x,y,z = t1
print(x,y,z)
t2= (1,2,3,1)
print(len(t2))
print(t2.count(1)) #contar numero de apariciones en la tupla
print(t2.index(2)) #posicion del valor