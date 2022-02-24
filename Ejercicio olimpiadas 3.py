peso=float(input("Ingrese peso: "))
altura=float(input("Ingrese altura: "))
imc=round(peso/altura**2,2)
print("El imc es: ", str(imc))