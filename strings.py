name = "juan"
last_name  = "marin"
age = 18

print(name)
print(last_name)

#concatenar
full_name = name +" "+  last_name
print(full_name)

frase = "I'm juan"
print(frase)

frase2 = 'She said"hello"'
print(frase2)

#manipular formato
template = "Hola, mi nombre es "+name+" y mi apellido es "+last_name
print('v1',template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2',template2)

template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3",template3)

#ejercicio
template4 = f"Hola, mi nombre es {name} mi apellido es {last_name} y mi edad es {age}"
print("v4",template4)