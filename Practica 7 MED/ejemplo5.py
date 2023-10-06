def dividir(a, b):
    if b == 0:
        raise ValueError("No puedes dividir por cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(e)
"""

"""
# EJERCICIO DE CLASE
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        if self.saldo == 0:
            raise ValueError("Su cuenta esta en 0")
        if cantidad < 0:
            raise ValueError("El monto a retirar no puede ser negativo.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        
        self.saldo -= cantidad
        print("Saldo retirado, su cuenta queda a: {}".format(self.saldo))