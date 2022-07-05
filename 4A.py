import string


def entrada(mensaje):
    num = int(input("Ingresa el " + mensaje + ": "))
    return num

def factorial(N):
    resultado = 1
    if (N < 0):
        print("Error el numero es negativo, por favor, vuelva a intentarlo")
    else:
        while (N > 0):
            resultado *= N
            N += -1
    return resultado

N = entrada("Numero")
resultadoFactorial = factorial(N)
print("El resultado del factorial es: " + str(resultadoFactorial))