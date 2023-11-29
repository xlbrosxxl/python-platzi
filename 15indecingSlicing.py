text = "Ella sabe Python"

#indixing mirar posiciones
print(text[0]) # E
print(text[1]) # l
print(text[9]) # " "
print(text[10]) # p

#saber cual es el ultimo caracter
#1 opcion, usando len
size = len(text)
print(size-1) # -1 por que empieza desde 0 y no desde 1

#2 opcion
print(text[-1]) #ultima pos


#slicing, sacar partes del texto
print(text[0:5]) #ella
print(text[10:16]) #python
print(text[:10]) # marcar que empieza desde 0
print(text[4:]) # marcar que llegue hasta el final
print(text[:]) # no marcar un limite
print(text[10:16:2]) # marcar el numero de saltos, PYTHON, P-T-O
print(text[::2])