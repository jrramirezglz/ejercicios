mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
otro_set = {1,2,3,4}
print(type(otro_set))
print(otro_set)

lista = [1,2,3,4,5,6,7,1,2,3,4,5]
print(lista)
li = set(lista)
print(li)
lista =list(li)
print(lista) 
set2 = set(('ramon','mariela', 'romina'))
print(set2)
set2 = set(('ramon','mariela', 'romina','ramon','mariela', 'romina'))
print(set2)
print(len(set2))
print('ramon' in set2)
s1 = set((1,2,3))
s2 = set((3,4,5))
s3 = s1.union(s2)
print(s3)

sa = set((1,2,3))
print(sa)
sa.add(4)
print(sa)
sa.remove(4)
print(sa)
sa.discard(3)
print(sa)
sa.pop()
print(sa)
sa = set((1,2,3))
print(sa)
sa.clear()
print(sa)