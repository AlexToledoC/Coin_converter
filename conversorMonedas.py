dolares = float(input("¿Cuántos dólares tienes?: "))
conversion = input("A qué criptomoneda deseas convertir? BTC (bitcoin) o ETH (ethereum). Escribe el respectivo símbolo: ")
bitcoin = 43987
ethereum = 3143
if conversion == "BTC" or conversion == "bitcoin" or conversion == "btc":
    btc = str(dolares / bitcoin)
    btc = str(btc)
    print("Tienes " + btc + "bitcoin")
elif conversion == "ETH" or conversion == "ethereum" or conversion == "eth":
    eth = str(dolares / ethereum)
    print("Tienes " + eth + "ether")
else:
    print("Ingresa una opción válida")
