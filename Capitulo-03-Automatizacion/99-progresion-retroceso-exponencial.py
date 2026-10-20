# Diapositiva 99: Retroceso exponencial, manejo de errores temporales
# Muestra la progresion de esperas del retroceso exponencial: cada espera
# es el doble de la anterior (1, 2, 4, 8, 16 segundos).

# Recorremos cinco intentos numerados del 0 al 4.
for intento in range(5):
    # La espera del intento n es 2 elevado a n: duplica cada vez.
    espera = 2 ** intento
    # Mostramos cuanto habria que esperar en este intento.
    print(f"intento {intento}: esperar {espera}s")

# Salida:
# intento 0: esperar 1s
# intento 1: esperar 2s
# intento 2: esperar 4s
# intento 3: esperar 8s
# intento 4: esperar 16s
