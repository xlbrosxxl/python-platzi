user_option = input("Ingrese 'piedra', 'papel' o 'tijera' ->")
user_option = user_option.lower()
computer_option = 'papel'

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

