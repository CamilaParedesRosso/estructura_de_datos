def factorial(numero):
    if numero>1:
        numero=numero*factorial(numero-1)
    return numero

print (factorial(5))
