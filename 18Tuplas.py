# no son mutables, no se pueden cambiar
numbers = (1,2,3,4,2)
text = ("juan","jose","nicolas")

print(numbers)
print(text)
print(type(numbers))

#acceder a un valor 
print(text[0]) #juan
print(text[-1]) #nicolas

#metodo de una tupla
#buscar elemento
print(text.index("juan")) #pos 0
print(numbers.count(2)) # 2 veces

#para cambiar un valor se cambia una tupla a lista
my_list = list(text)
print(my_list)
print(type(my_list))
#ahora ya se puede modificar la lista
my_list[1] = "karen"
print(my_list)

#convertir lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
