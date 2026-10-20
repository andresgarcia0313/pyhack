# Diapositiva 38: Comprensiones, filtrar y transformar en una linea
# Muestra el mismo filtro con for tradicional, con comprension de lista y con
# un generador que no construye la lista completa.

# Lista de puertos a clasificar.
puertos = [21, 22, 23, 80, 443, 3389, 8080]
# Conjunto de puertos inseguros (texto plano).
inseguros_texto_plano = {21, 23, 80}

# Forma tradicional: cuatro lineas.
# Lista vacia donde se guardaran los seguros.
seguros = []
# Recorre cada puerto.
for p in puertos:
    # Si el puerto NO esta entre los inseguros...
    if p not in inseguros_texto_plano:
        # ...lo agrega a la lista.
        seguros.append(p)

# Comprension de lista: una sola linea con el mismo resultado.
seguros_c = [p for p in puertos if p not in inseguros_texto_plano]
# Comprueba que ambas formas dan lo mismo y muestra el resultado.
print(seguros == seguros_c, seguros_c)

# Generador: (1 for ...) entrega los valores de a uno; sum los cuenta sin crear la lista.
print(sum(1 for p in puertos if p > 1024))
