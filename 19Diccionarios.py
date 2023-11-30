my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict = {
    'name':"juan",
    'avion':"blablabla",
    "last_name":"marin",
    "age":87
}
print(my_dict)

#cuantos elementos
print(len(my_dict))

#leer diccionario
print(my_dict["name"])
print(my_dict.get("age"))

#validar si esta
print("avion" in my_dict)
print("jose" in my_dict)