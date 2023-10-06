class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta.")
        self.saldo -= cantidad
        return cantidad
cuenta = CuentaBancaria(1000)

try:
    cantidad_retirada = cuenta.retirar(500)
    print("Se retiraron", cantidad_retirada, "de la cuenta.")
    print("Saldo restante:", cuenta.saldo)
except ValueError as e:
    print("Error:", str(e))
