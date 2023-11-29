#si
print("if")
if True:
    print("deberia funcionar")

if False:
    print("nunca va a funcionar")

pet = input("¿Cual es tu mascota favorita? ")
if pet == "Perro" or pet == "perro":
    print("tu mascota favorita es un perro")
elif pet == "Gato" or pet == "gato":
    print("tu mascota fav es un gato")
elif pet == "pez" or pet == "Pez":
    print("tu mascota es un pez")
else:
    print("tu mascota es otro tipo")
'''
stock = int(input("Ingrese el stock "))
if stock >= 100 and stock <= 1000:
    print(f"el stock de {stock} si esta en los limites")
else:
    print(f"el stock {stock} no esta en los limites")
'''
