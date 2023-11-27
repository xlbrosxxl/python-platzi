name = "juan"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

age = 12
print("Mi edad es "+str(age))
print(f"Mi edad es {age}")

age = int(input("Ingrese la edad:"))
print(type(age))
print(f"La edad ingresa es {age} años, y en 10 años tendras {age+10} años")

#ejercicio
name = input("ingrese su edad")
print(name)
age = int(input("ingrese su edad"))
print(age)

template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {age+10} años"
print(template)