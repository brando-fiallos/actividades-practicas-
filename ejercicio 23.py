with open('nombres.txt', 'a+') as f:
    while True:
        nombre = input("Nombre (o enter para salir): ").strip()
        if not nombre: break
        f.write(nombre.title() + '\n')