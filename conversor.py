def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

def cripto(cripto, valor_cripto):
    pesos = float(input("¿Cuánto " + cripto + " tienes?: "))
    dolares = (pesos * valor_cripto)/1
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas para saber cuántos dólares tienes🤑

1. pesos colombianos
2. pesos argentinos
3. pesos mexicanos
4. bitcoin
5. ethereum

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 60)
elif opcion == 3:
    conversor("mexicanos", 20)
elif opcion == 4:
    cripto("bticoin", 44626)
elif opcion == 5:
    cripto("ethereum", 3145)
else:
    print("Por favor escoge una opción correcta")