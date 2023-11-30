'''
ciclo infinito

while True:
    print("se ejecuto")

contador = 0
while(contador < 10):
    contador+=1
    print(f"el contador va en {contador}")

contador = 0
while (contador < 20):
    contador += 1
    if(contador == 15):
        break
    print(contador)
'''

contador = 0
while contador < 20:
    contador+=1
    if contador < 15:
        continue
    print(contador)