#CRUD, Create, Read, Update, Delete
numbers = [1,2,3,4,5] #create
print(numbers[1]) #read
numbers[-1] = 10 #update
print(numbers)

#agregar elemento
numbers.append(700) #se agrega al final
print(numbers)

numbers.insert(0,100) #agrega donde se quiere, 1 parametro pos, 2 parametro valor
print(numbers)

numbers.insert(3,"hola") #en caso de que ya se tenga valores en una pos, se corren hacia la derecha
print(numbers)

#unir listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

#actualizar
print(new_list.index("todo 2")) #saber en que pos esta
new_list[9] = "cambio"
print(new_list)

#eliminar
new_list.remove("todo 1") #eliminar elemento en especifico
print(new_list)

new_list.pop() #eliminar el ultimo
print(new_list)

new_list.pop(0) #eliminar pop con pos
print(new_list)


#voltear un array
new_list.reverse()
print(new_list)

#ordenar
numeros = [1,3,2,6,4]
numeros.sort()
print(numeros)

string = ["re", "Ab", "ed"]
string.sort()
print(string)