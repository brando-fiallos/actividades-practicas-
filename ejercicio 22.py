contador = 0
with open("nombres.txt", "r") as archivo:
    for nombre in archivo:
        if nombre.strip().startswith("l"):
            contador += 1
print(f"Nombres que empiezan con 'l': {contador}")