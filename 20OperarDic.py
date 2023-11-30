persona = {
    "name" : "juan",
    "last_name":"marin",
    "languajes":["python","JS"],
    "age":18
}
print(persona)

#actualizar un atributo 
persona["name"] = "jose"
persona["age"] -= 8
persona["languajes"].append("rust")
print(persona)

#eliminar un atributo
del persona["last_name"]
print(persona)

persona.pop("age")
print(persona)

#mirar los items
print("items")
print(persona.items())

print("keys")
print(persona.keys())

print("values")
print(persona.values())