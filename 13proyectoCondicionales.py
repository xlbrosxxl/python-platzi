#importar ramdom
import random

#crear tupla con las opciones para la computadora
options = ("piedra","papel","tijera")

#ingresar opciones de el usuario
user_option = input("Ingrese 'piedra', 'papel' o 'tijera' ->")

#convertir la opcion en minusculas
user_option = user_option.lower()

if not(user_option in options):
    print("la opcion no es valida")
computer_option = random.choice(options)

#mostrar las opciones
print(f"useroption -> {user_option}")
print(f"console option -> {computer_option}")

if(user_option == computer_option):
    print("¡EMPATE!")
elif(user_option == 'piedra'):
    if(computer_option == 'tijera'):
        print("jugador gana")
    else:
        print("pc gana")
elif(user_option == 'papel'):
    if(computer_option == 'piedra'):
        print("jugador gana")
    else:
        print("pc gana")
elif(user_option == 'tijera'):
    if(computer_option == 'papel'):
        print("jugador gana")
    else:
        print("pc gana")
else:
    print("ingrese una opcion valida")

