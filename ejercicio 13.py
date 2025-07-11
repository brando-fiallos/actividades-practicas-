#reescriba el calculo de su salario con una hora y media para las horas extras
#cree un afuncion llamada computepay (calcular salario) que toma 2 parametros (horas y tarifa )

horas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

def computepay(horas, tarifa):
    if horas > 40:  # Si hay horas extras
        horas_extras = horas - 40
        pago_normal = 40 * tarifa
        pago_extras = horas_extras * (tarifa * 1.5)  
        total_pago = pago_normal + pago_extras
    else:
        total_pago = horas * tarifa
    
    return total_pago


salario = computepay(horas, tarifa)
print(f"El salario total es: ${salario:.2f}")