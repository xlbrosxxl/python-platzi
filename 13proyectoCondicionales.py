#importar ramdom
import random
rondas = 1
win_pc = 0
win_jg = 0
#crear tupla con las opciones para la computadora
options = ("piedra","papel","tijera")

while True:
    print("*"*10)
    print("¡RONDA N!",rondas)
    print("ganadas del jugador",win_jg)
    print("ganadas del pc",win_pc)
    print("*"*10)

    if(win_jg == 2):
        print("EL JUGADOR GANA")
        break
    elif(win_pc == 2):
        print("EL PC GANA")
        break
    
    rondas += 1
    #ingresar opciones de el usuario
    user_option = input("Ingrese 'piedra', 'papel' o 'tijera' ->")

    #convertir la opcion en minusculas
    user_option = user_option.lower()

    #darle una opcion random a la pc
    computer_option = random.choice(options)

    #mostrar las opciones
    print(f"useroption -> {user_option}")
    print(f"console option -> {computer_option}")   

    #realizar comprobaciones para saber si se gana o no
    if(user_option == computer_option):
        print("¡EMPATE!")
    elif(user_option == 'piedra'):
        if(computer_option == 'tijera'):
            print("jugador gana")
            win_jg+=1
        else:
            print("pc gana")
            win_pc+=1
    elif(user_option == 'papel'):
        if(computer_option == 'piedra'):
            print("jugador gana")
            win_jg+=1
        else:
            print("pc gana")
            win_pc+=1
    elif(user_option == 'tijera'):
        if(computer_option == 'papel'):
            print("jugador gana")
            win_jg+=1
        else:
            print("pc gana")
            win_pc+=1
    else:
        print("ingrese una opcion valida")
        continue