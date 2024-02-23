cliente = {'nombre': 'Juan', 'apellido':'Fuentes','peso':88}
consulta = (cliente['apellido'])
print(consulta)#Fuentes

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])#20
print(dic['c3']['s2'])#200
dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())#E
dic = {1:'a',2:'b'}
print(dic)#{1: 'a', 2: 'b'}
dic[3]='c'
print(dic)#{1: 'a', 2: 'b', 3: 'c'}
dic[2]= 'B'
print(dic)#{1: 'a', 2: 'B', 3: 'c'}
print(dic.keys())#dict_keys([1, 2, 3])
print(dic.values())#dict_values(['a', 'B', 'c'])
print(dic.items())#dict_items([(1, 'a'), (2, 'B'), (3, 'c')])
