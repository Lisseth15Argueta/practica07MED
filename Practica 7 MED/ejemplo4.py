try:
    a = int(input("Digite el primer numero: "))
    b = int(input("Digite el segundo numero: "))
    resultado = a / b
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
else:
    print("El resultado es:", resultado)
finally:
    print("Operación finalizada.")