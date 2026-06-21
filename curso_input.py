#palabra=input("Introduce una palabra:")
nu1=input("Introduce un numero:")
try:
    nu1=int(nu1)
except ValueError:
    print("Esto no es un numero")
    exit()
print(f"Esto es un numero: {nu1}")