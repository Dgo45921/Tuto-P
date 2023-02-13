numero1 = float(input("Dame un número:"))
numero2 = float(input("Dame otro número:"))
operacion = input("¿Qué operación desea hacer? Coloque 1 si deseas sumarlos, 2 si desea restarlos, 3 si desea "
                  "multiplicarlos o 4 si desea multiplicarlos:")

if operacion == "1":
    print(numero1+numero2)
elif operacion == "2":
        if numero1 > numero2:
            print(numero1-numero2)
        elif numero1 < numero2:
            print(-1*(numero1-numero2))
        else:
            print("0")
elif operacion == "3":
    print(numero1/numero2)
elif operacion == "4":
    print(numero1/numero2)
else:
    print("No se puede efectuar la operación")