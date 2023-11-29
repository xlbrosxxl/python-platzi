text = "Ella sabe programar en Python"

#buscar algo dentro del texto
print("JavaScript" in text)
print("Python" in text)

if ("Python" in text):
    print("Si esta en el texto")
else:
    print("No esta en el texto")

#tamaño de un string, los espacios cuenta como caracter
tamaño = len("amor ")
print(tamaño)
size = len(text)
print(size)

#volver mayuscula y minuscula
print(text)
print(text.upper())
print(text.lower())

#numero de apericiones de una letra en el texto
print(text.count('a'))

#transformar mayus a minus y minus a mayus
print(text.swapcase())

#mirar con que empieza un texto
print(text.startswith("Ella"))

#mirar con que termina un texto
print(text.endswith("Rust"))

#reemplazar en el texto
print(text.replace("Python", "Go"))

text2 = "este es un titulo"
print(text2)

#1 caracter en mayusc
print(text2.capitalize())

#cada espacio en mayusc
print(text2.title())

#saber si es un digito
print(text2.isdigit())
print("31212".isdigit())

