import datetime
def fibonacci_recusivo(n):
    if n < 2:
        return n
    else:
        return fibonacci_recusivo(n - 1) + fibonacci_recusivo(n - 2)
def fibonacci_bulces(n):
    f = 0
    for x in range(n):
        f += (x-1)+(x-2)
    return f
inicio_r = datetime.datetime.now()
print(fibonacci_recusivo(40))
fin_r = datetime.datetime.now()
print("El tiempo de ejecución de la funcion recursiva es:", fin_r - inicio_r)
inicio_b = datetime.datetime.now()
print(fibonacci_recusivo(40))
fin_b = datetime.datetime.now()
print("El tiempo de ejecución del bucle:", fin_b - inicio_b)



