
import Operaciones

print("====== CALCULADORA EN PYTHON ======")

try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    print("\nSeleccione la operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        resultado = Operaciones.sumar(numero1, numero2)

    elif opcion == "2":
        resultado = Operaciones.restar(numero1, numero2)

    elif opcion == "3":
        resultado = Operaciones.multiplicar(numero1, numero2)

    elif opcion == "4":
        resultado = Operaciones.dividir(numero1, numero2)

    else:
        resultado = "Opcion no valida."

    print("\nResultado:", resultado)

except ValueError:
    print("Error: Debe ingresar numeros validos.")
