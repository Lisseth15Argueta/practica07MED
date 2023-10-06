try:
    valor = int(input("Ingrese un número: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debe ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
else:
    print("El resultado es:", resultado)