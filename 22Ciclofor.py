'''
for element in range(1,21):
    print(element)
'''
my_list = [23,45,67,89,43]
for i in my_list:
    print(i)

my_tuple = ("hola","buenas","juan")
for i in my_tuple:
    print(i)

my_dict = {
    "name":"juan",
    "age":18,
    "languajes":["java","python","go"]
}
for i in my_dict:
    print("key->", i,"valor ->",my_dict[i])

#otra forma
for key, value in my_dict.items():
    print(key,"=>",value)

people = [
    {
        "name":"nico",
        "age":34
    },
    {
        "name":"zule",
        "age":45
    },
    {
        "name":"santi",
        "age":4
    }
]

for elemento in people:
    print(elemento)
    print("nombre ->",elemento["name"])