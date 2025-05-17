massa=float(input("digite sua massa: "))
altura=float(input("digite sua altura: "))
imc=massa/(altura**2)
print("seu imc é:", imc)

if imc<18.5:
    print("abaixo do peso")
elif imc<25:
    print("peso normal")
elif imc<30:
    print("sobrepeso")
else:
    print("obesidadel")