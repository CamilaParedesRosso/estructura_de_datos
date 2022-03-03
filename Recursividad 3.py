def factorial(numero):
    if numero>1:
        numero=numero*factorial(numero-1)
    return numero
n=int(input("Ingrese el numero: "))
if n==0:
    print("Factorial de 0 es 1.")
else:
    print (factorial(n))
