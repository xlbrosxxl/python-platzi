matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
        ]

#obtener la lista
print(matriz[0])
print(matriz[1])
print(matriz[2])

#obtener el valor
print(matriz[0][1]) #fila 0, columna 1, = 2

for row in matriz:
    print(row)
    for column in row:
        print(column)