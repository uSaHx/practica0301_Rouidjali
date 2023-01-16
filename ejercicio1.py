import datetime
def fibonacci_recusivo(n):
    if n < 2:
        return n
    else:
        return fibonacci_recusivo(n - 1) + fibonacci_recusivo(n - 2)
def fibonacci_bulces(numero):
    n1, n2 = 0, 1
    count = 0
    if numero <= 0:
       print("Error")
    elif numero == 1:
       print(n1)
    else:
       while count < numero:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
    return
inicio_r = datetime.datetime.now()
fibonacci_recusivo(40)
fin_r = datetime.datetime.now()
print("El tiempo de ejecución del bucle:", fin_r - inicio_r)
inicio_b = datetime.datetime.now()
fibonacci_bulces(40)
fin_b = datetime.datetime.now()
print("El tiempo de ejecución del bucle:", fin_b - inicio_b)



