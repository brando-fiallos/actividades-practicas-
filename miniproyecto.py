# Calculadora de propina básica
cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina (10, 15, 20): "))

propina = cuenta * (porcentaje / 100)
total = cuenta + propina

print("\nResumen:")
print(f"Cuenta: ${cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")