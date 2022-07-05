def entrada(mensaje):
    num = int(input("Ingresa " + mensaje + ": "))
    return num

def conjuntoNumeros(numero):
    if (numero < 0):
        num = numero
    else:
        print("El numero es positivo, intente de nuevo")
        num = 0
    return num
        

def promedioNegativos(suma, N):
    promedio = suma / N
    return promedio

N = entrada("la cantidad de elementos del conjunto")
Naux = N
suma = 0
while(Naux > 0):
    num = int(input("Ingresa un numero del conjunto"))
    suma += conjuntoNumeros(num)
    Naux += -1

promedio = promedioNegativos(suma, N)
print("El promedio de los numeros negativos del conjunto es: " + str(promedio))