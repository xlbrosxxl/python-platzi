x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x==y)

#primer metodo para convertir y
y_str = format(y,".2g")
print("str =>", y_str)
print(y_str == str(x))

#segundo metodo usando mat
tolerancia = 0.0001
print(abs(x - y) < tolerancia)