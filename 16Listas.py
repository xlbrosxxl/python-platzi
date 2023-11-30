numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))

tasks = ["levantarme", "aprender", "dormir"]
print(tasks)

#las listas pueden tener varios tipos de datos
types = [1, True, "hola"]
print(types)

print(numbers[0])
print(tasks[0])

'''
los strings no son mutables cambianbles
text = "hola"
text[0] = "w"
print(text)
'''

#cambiar un elemento
tasks[0] = "ver tv"
print(tasks)

print(numbers[:3])

print(True in types)
print("hola" in types)
